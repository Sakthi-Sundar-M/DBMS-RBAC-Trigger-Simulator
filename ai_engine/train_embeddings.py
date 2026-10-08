"""
Contrastive Fine-Tuning Script for DBMS Trigger & RBAC Semantic Evaluator
Model Base: sentence-transformers/all-MiniLM-L6-v2 (22 Million Parameters)
Hardware: Standard Laptop CPU (Optimized for low RAM / CPU execution)
Architecture: Selective Layer Fine-Tuning (Top 2 layers + Pooling Head)
"""

import os
import gc
import json
import torch
from sentence_transformers import SentenceTransformer, InputExample, losses

def load_training_data(dataset_paths=None):
    """
    Constructs anchor, positive, and negative contrastive pairs
    from curated exam questions and PYQs.
    """
    if dataset_paths is None:
        dataset_paths = ["data/exam_questions.json", "data/comprehensive_pyqs.json"]

    questions_map = {}
    for path in dataset_paths:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    q_list = json.load(f)
                    for q in q_list:
                        qid = q.get("id") or q.get("title")
                        if qid and qid not in questions_map:
                            questions_map[qid] = q
            except Exception as e:
                print(f"Warning: Failed loading {path}: {e}")

    questions = list(questions_map.values())
    print(f"Loaded {len(questions)} unique questions across datasets.")

    train_examples = []

    for i, q in enumerate(questions):
        sol = q.get("solution_key", "")
        exp = q.get("ground_truth_explanation", "")
        prompt = q.get("prompt", "")

        if not sol:
            continue

        # 1. Positive Pairs (High Semantic Similarity: 0.85 - 0.95)
        if exp:
            train_examples.append(InputExample(
                texts=[sol, f"Relational database solution for {q.get('title', '')}: {exp}"],
                label=0.95
            ))
        if prompt:
            train_examples.append(InputExample(
                texts=[prompt, sol],
                label=0.85
            ))

        # 2. Domain Hard Negative Pairs (Subtle Invariants: 0.05 - 0.20)
        if "BEFORE" in sol:
            train_examples.append(InputExample(
                texts=[sol, sol.replace("BEFORE", "AFTER")],
                label=0.15
            ))
        if "NEW" in sol:
            train_examples.append(InputExample(
                texts=[sol, sol.replace("NEW", "OLD")],
                label=0.10
            ))
        if "GRANT" in sol:
            train_examples.append(InputExample(
                texts=[sol, sol.replace("GRANT", "REVOKE")],
                label=0.10
            ))
        if "FOR EACH ROW" in sol:
            train_examples.append(InputExample(
                texts=[sol, sol.replace("FOR EACH ROW", "FOR EACH STATEMENT")],
                label=0.15
            ))
        if "RETURN NEW" in sol:
            train_examples.append(InputExample(
                texts=[sol, sol.replace("RETURN NEW", "RETURN NULL")],
                label=0.10
            ))

        # 3. Cross-question Negative Pairs (Different topics)
        other_q = questions[(i + len(questions) // 2) % len(questions)]
        other_sol = other_q.get("solution_key", "")
        if other_sol and other_sol != sol:
            train_examples.append(InputExample(
                texts=[sol, other_sol],
                label=0.05
            ))

    return train_examples


def train_evaluator_model(
    output_dir: str = "models/dbms-trigger-evaluator",
    num_epochs: int = 2,
    batch_size: int = 4
):
    print("=" * 70)
    print("LIGHTWEIGHT AI MODEL TRAINING: DBMS TRIGGERS & RBAC EVALUATOR")
    print("=" * 70)

    # Restrict thread count to prevent memory fragmentation and thread contention on CPU
    torch.set_num_threads(2)

    print("Loading Base Model: sentence-transformers/all-MiniLM-L6-v2 on CPU...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    model.max_seq_length = 96  # Optimized for crisp code and explanations

    # Memory Optimization: Freeze embeddings and layers 0-3; train layers 4 & 5
    for name, param in model.named_parameters():
        if "layer.0." in name or "layer.1." in name or "layer.2." in name or "layer.3." in name or "embeddings." in name:
            param.requires_grad = False

    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Transfer Learning: {trainable_params:,} trainable params ({trainable_params/total_params*100:.1f}% of total).")

    train_examples = load_training_data()
    print(f"Generated {len(train_examples)} contrastive training pairs.")

    loss_fn = losses.CosineSimilarityLoss(model=model)
    optimizer = torch.optim.AdamW(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=3e-5
    )

    print(f"Starting Contrastive Fine-Tuning ({num_epochs} Epochs, Batch Size {batch_size})...")
    model.train()
    for epoch in range(num_epochs):
        total_loss = 0.0
        steps = 0
        for i in range(0, len(train_examples), batch_size):
            batch = train_examples[i:i + batch_size]
            texts1 = [ex.texts[0] for ex in batch]
            texts2 = [ex.texts[1] for ex in batch]
            labels = torch.tensor([ex.label for ex in batch], dtype=torch.float32)

            feat1 = model.tokenize(texts1)
            feat2 = model.tokenize(texts2)

            optimizer.zero_grad(set_to_none=True)
            loss = loss_fn([feat1, feat2], labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            steps += 1

            del feat1, feat2, loss
            if steps % 30 == 0:
                gc.collect()

        avg_loss = total_loss / max(1, steps)
        print(f"Epoch {epoch + 1}/{num_epochs} Complete. Average Contrastive Loss: {avg_loss:.4f}")

    os.makedirs(output_dir, exist_ok=True)
    model.save(output_dir)
    gc.collect()
    print("=" * 70)
    print(f"Training Complete! Customized model weights saved to: {output_dir}")
    print("=" * 70)


if __name__ == "__main__":
    train_evaluator_model()
