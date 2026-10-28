# ai_engine/mcq_data.py
# Curated Indian Entrance Exam MCQs (GATE, ISRO, NIELIT, UGC-NET)

MCQ_BENCHMARK_QUESTIONS = [
  {
    "id": "MCQ-001",
    "title": "B+ Tree Root Node Occupancy Relaxation Invariant",
    "topic": "Indexing & Storage",
    "subtopic": "B+ Tree Node Occupancy Invariants",
    "difficulty": "Easy",
    "source": "GATE CSE 2024 Set 1 | Question: 21 (PYQs/CS124S5.pdf, Page 15)",
    "source_file": "PYQs/CS124S5.pdf",
    "source_page": 15,
    "source_qnum": "Q.21",
    "evidence_snippet": "Q.21 In a B+ tree, the requirement of at least half-full (50%) node occupancy is relaxed for which one of the following cases? (A) Only the root node (B) All leaf nodes",
    "prompt": "In a B+ tree of order p, the requirement of at least half-full (50%) node occupancy is relaxed for which one of the following cases?",
    "options": [
      "A. Only the root node",
      "B. All leaf nodes",
      "C. All internal nodes except the root",
      "D. Only the leftmost leaf node"
    ],
    "correct_option": "A",
    "explanation": "In a standard B+ tree of order p, every internal node must maintain at least ceil(p/2) pointers and every leaf node must maintain at least ceil((p-1)/2) keys to prevent underflow. The only structural exception is the root node: if it is an internal node, it may have as few as 2 children (1 key); if it is the only node in the tree, it may have fewer keys.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A clinical oncology EHR system indexes patient genomic sequencing variants using a B+ tree of order 64. When the index is freshly initialized with low patient volume, which node is exempt from the half-full node filling constraint?",
        "options": [
          "A. All terminal leaf nodes storing biopsy gene markers",
          "B. Any interior index node pointing to pediatric cancer profiles",
          "C. Only the root node of the genomic variant tree",
          "D. The leftmost node holding wild-type reference alleles"
        ],
        "correct_option": "C",
        "explanation": "B+ tree structural balancing relaxes the 50% occupancy rule exclusively for the root node, which can hold as few as 2 child pointers."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated clearinghouse (ACH) wire settlement B+ tree index of order 128, which node is legally permitted by the database storage engine to hold only 2 child pointers without triggering a page merge or rebalancing operation?",
        "options": [
          "A. Any leaf node holding intra-bank transfer records",
          "B. Only the root node of the wire settlement index",
          "C. All internal routing nodes along the search path",
          "D. The rightmost leaf node holding the current day's unsettled batches"
        ],
        "correct_option": "B",
        "explanation": "Only the root node is exempt from the 50% minimum occupancy invariant; all other internal nodes must retain at least ceil(p/2) child pointers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a high-throughput flash-sale checkout database indexing 10 million order records via a B+ tree of order 200, which node in the index structure is structurally permitted to contain fewer than ceil(p/2) child pointers without triggering an underflow merge?",
        "options": [
          "A. Any leaf node pointing to recently added product catalog SKUs",
          "B. Only the root node of the order index",
          "C. Every internal node located at level 1 below the root",
          "D. Only the rightmost leaf node receiving live checkout inserts"
        ],
        "correct_option": "B",
        "explanation": "In a B+ tree of order p, all internal nodes except the root must maintain at least ceil(p/2) child pointers. The root node alone is permitted to hold as few as 2 pointers (or 1 key if non-leaf) without violating B+ tree invariants."
      }
    ]
  },
  {
    "id": "MCQ-002",
    "title": "First Normal Form (1NF) Composite Attribute Invariants",
    "topic": "Normalization & Functional Dependencies",
    "subtopic": "First Normal Form Invariants",
    "difficulty": "Medium",
    "source": "GATE CSE 2024 Set 1 | Question: 22 (PYQs/CS124S5.pdf, Page 15)",
    "source_file": "PYQs/CS124S5.pdf",
    "source_page": 15,
    "source_qnum": "Q.22",
    "evidence_snippet": "Q.22 Which of the following statements about a relation R in first normal form (1NF) is/are TRUE ? (A) R can have a multivalued attribute (B) R can have a composite attribute",
    "prompt": "Which of the following statements about a relation R in first normal form (1NF) is TRUE?",
    "options": [
      "A. R can have a multi-valued attribute",
      "B. R can have a composite attribute",
      "C. All attributes in R must be part of some candidate key",
      "D. Every attribute in R must be atomic and non-divisible"
    ],
    "correct_option": "D",
    "explanation": "First Normal Form (1NF) mandates that the domain of each attribute must contain only atomic (indivisible) values and that the value of each attribute in every tuple must be a single value from that domain. Consequently, multi-valued attributes and composite attributes are strictly prohibited in 1NF.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an intensive care EMR database, a nurse notes that a table Patient_Vitals stores hourly blood pressure readings as an array within a single cell. Why does this violate First Normal Form (1NF)?",
        "options": [
          "A. Because 1NF permits only alphanumeric text data types",
          "B. Because 1NF requires a foreign key referencing the attending physician",
          "C. Because 1NF strictly requires every attribute value in every tuple to be indivisible and atomic",
          "D. Because patient vitals must be indexed using a multi-way B-tree"
        ],
        "correct_option": "C",
        "explanation": "Storing an array or list of values inside a single tuple attribute violates the atomicity requirement of 1NF."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A core banking customer ledger table Customer_KYC is evaluated for 1NF compliance under financial compliance rules. What condition must hold for Customer_KYC to satisfy 1NF?",
        "options": [
          "A. All non-key attributes must be fully functionally dependent on customer credit rating",
          "B. Customer contact numbers can be stored as comma-delimited arrays in a single column",
          "C. Customer residential address can be stored as an indivisible composite struct without flattening",
          "D. Every column must hold atomic scalar values, and multi-valued phone or address lists must be normalized"
        ],
        "correct_option": "D",
        "explanation": "1NF disallows composite and multi-valued fields; every field must hold strictly single atomic values."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce order table Order_Shipments stores multiple package tracking numbers as a comma-separated text string inside a single tracking_numbers column for each order. Under relational database theory, which normal form is directly violated?",
        "options": [
          "A. Second Normal Form (2NF) due to partial dependency",
          "B. Third Normal Form (3NF) due to transitive dependency",
          "C. Boyce-Codd Normal Form (BCNF) due to non-superkey determinants",
          "D. First Normal Form (1NF) due to non-atomic multi-valued attribute values"
        ],
        "correct_option": "D",
        "explanation": "1NF requires all attribute values to be atomic and indivisible. Storing a comma-separated list or array of tracking numbers in a single column violates 1NF."
      }
    ]
  },
  {
    "id": "MCQ-003",
    "title": "Armstrong Axioms and Functional Dependency Deduction",
    "topic": "Functional Dependencies",
    "subtopic": "Inference Rules & Axioms",
    "difficulty": "Medium",
    "source": "GATE CSE 2024 Set 1 | Question: 44 (PYQs/CS124S5.pdf, Page 28)",
    "source_file": "PYQs/CS124S5.pdf",
    "source_page": 28,
    "source_qnum": "Q.44",
    "evidence_snippet": "Q.44 The symbol → indicates functional dependency in the context of a relational database. Which of the following options is/are always TRUE?",
    "prompt": "Let X, Y, Z be sets of attributes in a relational schema, and -> denote functional dependency. According to Armstrong's Axioms and sound inference rules, which of the following is always TRUE?",
    "options": [
      "A. If X -> Y and Y -> Z, then X -> Z (Transitivity)",
      "B. If X -> Y, then XZ -> YZ for any attribute set Z (Augmentation)",
      "C. If X -> Y and X -> Z, then X -> YZ (Union rule)",
      "D. All of the above (Transitivity, Augmentation, and Union rules are all sound)"
    ],
    "correct_option": "D",
    "explanation": "Armstrong's Axioms consist of three primary sound and complete inference rules: Reflexivity (if Y ⊆ X, then X -> Y), Augmentation (if X -> Y, then XZ -> YZ), and Transitivity (if X -> Y and Y -> Z, then X -> Z). From these, secondary rules such as the Union rule (if X -> Y and X -> Z, then X -> YZ) and Decomposition rule are derived. Hence, all listed rules are sound and always true.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR clinical database, Doctor_ID -> Hospital_Wing and Doctor_ID -> Department hold. Which derived inference rule guarantees that Doctor_ID functionally determines {Hospital_Wing, Department}?",
        "options": [
          "A. Decomposition Rule",
          "B. Reflexivity Axiom",
          "C. Augmentation Rule",
          "D. Union Rule (Composition of functional dependencies)"
        ],
        "correct_option": "D",
        "explanation": "The Union rule states that if X -> Y and X -> Z, then X -> YZ."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A bank's transaction schema evaluates dependencies across Account_ID, Customer_ID, and Credit_Rating. If Account_ID -> Customer_ID and Customer_ID -> Credit_Rating hold, which rule guarantees Account_ID -> Credit_Rating?",
        "options": [
          "A. Transitivity Axiom (Armstrong's sound inference rule)",
          "B. Reflexivity Axiom",
          "C. Pseudo-transitivity Rule",
          "D. Augmentation Axiom"
        ],
        "correct_option": "A",
        "explanation": "By the transitivity axiom, X -> Y and Y -> Z implies X -> Z."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce catalog schema with dependencies SKU -> Category and SKU -> UnitPrice, which Armstrong inference rule proves that SKU -> Category, UnitPrice?",
        "options": [
          "A. Decomposition Rule",
          "B. Augmentation Axiom",
          "C. Reflexivity Axiom",
          "D. Union Rule (Composition of functional dependencies)"
        ],
        "correct_option": "D",
        "explanation": "The Union rule of functional dependencies states that if X -> Y and X -> Z, then X -> YZ."
      }
    ]
  },
  {
    "id": "MCQ-004",
    "title": "Relational Division and Subquery Tuple Cardinality",
    "topic": "SQL & Relational Algebra",
    "subtopic": "Relational Division & Universal Quantification",
    "difficulty": "Hard",
    "source": "GATE CSE 2025 Set 1 | Question: 39 (PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf, Page 39)",
    "source_file": "PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf",
    "source_page": 39,
    "source_qnum": "Q.39",
    "evidence_snippet": "Q.39 Consider two relations describing teams and players in a sports league: teams(tid, tname), players(pid, pname, tid)",
    "prompt": "Consider two relations describing teams and players: Teams(tid, tname) and Players(pid, pname, tid). A query is designed to find all teams that have players registered for every position in a reference table Positions(pos_name). In relational algebra, which algebraic construct precisely captures this universal quantification condition?",
    "options": [
      "A. Natural Join (⨝)",
      "B. Relational Division (÷)",
      "C. Outer Union (⊎)",
      "D. Left Outer Join (⟕)"
    ],
    "correct_option": "B",
    "explanation": "Universal quantification ('for all' / 'for every') in relational algebra is computed using the Relational Division operator (÷). In this scenario, dividing the projected player-team position mapping by the set of all available positions produces exactly those team IDs that match all positions in the divisor relation.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital credentialing committee writes a query to find surgeons who are certified across every surgical procedure listed in Mandatory_Procedures(proc_id). Which relational algebra operator expresses this condition without aggregation?",
        "options": [
          "A. Intersection (∩)",
          "B. Semijoin (⋉)",
          "C. Left Outer Join (⟕)",
          "D. Relational Division (÷)"
        ],
        "correct_option": "D",
        "explanation": "Relational division produces tuples in R that are associated with all tuples in S."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A central bank regulatory audit query must find all commercial banking institutions that have successfully submitted regulatory filings for every required compliance month in Compliance_Months(month_id). Which relational operator executes this universal requirement?",
        "options": [
          "A. Cartesian Product (×)",
          "B. Theta Join (⋈_θ)",
          "C. Relational Division (÷)",
          "D. Full Outer Join (⟗)"
        ],
        "correct_option": "C",
        "explanation": "Relational division (÷) models universal quantification ('all / every') across relational tuples."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce analytics team wants to find all Customer_IDs who have purchased items from EVERY vendor present in the Featured_Vendors table. Which relational algebra operator directly computes this universal quantification query?",
        "options": [
          "A. Theta Join (⋈_θ)",
          "B. Relational Division (÷)",
          "C. Cartesian Product (×)",
          "D. Outer Union (⊎)"
        ],
        "correct_option": "B",
        "explanation": "Relational division (R ÷ S) expresses queries with universal quantification ('for all' / 'every'), such as customers who purchased from all vendors in S."
      }
    ]
  },
  {
    "id": "MCQ-005",
    "title": "Candidate Keys and BCNF Decomposition of Functional Schemas",
    "topic": "Normalization & Functional Dependencies",
    "subtopic": "BCNF Decomposition & Keys",
    "difficulty": "Medium",
    "source": "GATE CSE 2025 Set 1 | Question: 47 (PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf, Page 47)",
    "source_file": "PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf",
    "source_page": 47,
    "source_qnum": "Q.47",
    "evidence_snippet": "Q.47 Consider a relational schema team(name, city, owner), with functional dependencies {name→city, name→owner}.",
    "prompt": "Consider a relational schema Team(name, city, owner) with functional dependencies F = {name -> city, name -> owner}. Which one of the following statements is CORRECT regarding the schema?",
    "options": [
      "A. The candidate key is {name}, and the schema is in 3NF and BCNF",
      "B. The candidate key is {name, city}, and the schema violates 2NF",
      "C. The candidate key is {owner}, and the schema is in 1NF only",
      "D. The schema violates BCNF because owner is transitively dependent on city"
    ],
    "correct_option": "A",
    "explanation": "Computing the attribute closure of name: {name}+ = {name, city, owner} = Team. Since name determines all attributes and is minimal, {name} is the sole candidate key. For every non-trivial functional dependency (name -> city and name -> owner), the left-hand side {name} is a superkey. Therefore, the relation satisfies the definition of Boyce-Codd Normal Form (BCNF) and Third Normal Form (3NF).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital pharmacy relation Drug_Supplier(drug_code, manufacturer_city, license_holder) has FDs {drug_code -> manufacturer_city, drug_code -> license_holder}. What is the highest normal form of this table?",
        "options": [
          "A. 2NF but not 3NF",
          "B. 3NF but not BCNF",
          "C. BCNF and 3NF, since the determinant drug_code is the candidate key for all non-trivial FDs",
          "D. 1NF only"
        ],
        "correct_option": "C",
        "explanation": "Every functional dependency has the candidate key drug_code on its LHS, satisfying BCNF."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A fintech ledger schema Merchant_Branch(merchant_id, headquarters_city, primary_bank) satisfies FDs: merchant_id -> headquarters_city and merchant_id -> primary_bank. In which normal form does this schema reside?",
        "options": [
          "A. It is in 2NF only because city and bank are non-prime attributes",
          "B. It is in BCNF and 3NF because merchant_id is a superkey for every functional dependency",
          "C. It violates 3NF due to transitive dependency across bank and city",
          "D. It is in 1NF only because merchant_id has multiple dependents"
        ],
        "correct_option": "B",
        "explanation": "Since merchant_id is a superkey, all FDs have superkeys on their LHS, meeting BCNF directly."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce inventory schema has relation Warehouse_Zone(Zone_Code, Aisle_Number, Supervisor_ID) with functional dependency Zone_Code -> Aisle_Number, Supervisor_ID. If Zone_Code is the only candidate key, in which highest normal form is the relation?",
        "options": [
          "A. BCNF (and therefore also 3NF and 2NF)",
          "B. 1NF only, because Zone_Code contains alphabetic characters",
          "C. 2NF only, due to partial functional dependencies",
          "D. 3NF only, because Supervisor_ID is not a superkey"
        ],
        "correct_option": "A",
        "explanation": "Since the determinant Zone_Code of every functional dependency is a superkey, the relation trivially satisfies Boyce-Codd Normal Form (BCNF) and 3NF."
      }
    ]
  },
  {
    "id": "MCQ-006",
    "title": "Candidate Key Minimal Closure for Multi-Attribute Relational Schema",
    "topic": "Functional Dependencies & Keys",
    "subtopic": "Candidate Key Minimal Closure",
    "difficulty": "Hard",
    "source": "GATE DA 2024 | Question: 17 (PYQs/DA_extracted/DA/DA2024.pdf, Page 16)",
    "source_file": "PYQs/DA_extracted/DA/DA2024.pdf",
    "source_page": 16,
    "source_qnum": "Q.17",
    "evidence_snippet": "Q.17 Let R(A,B,C,D,E) be a relational schema with functional dependency set F = {A -> BC, CD -> E, B -> D, E -> A}. Which of the following is a candidate key?",
    "prompt": "Let R(A, B, C, D, E) be a relational schema with functional dependency set F = {A -> BC, CD -> E, B -> D, E -> A}. Which of the following is a candidate key for R?",
    "options": [
      "A. {A}",
      "B. {B}",
      "C. {C}",
      "D. {D}"
    ],
    "correct_option": "A",
    "explanation": "Let us compute the attribute closure of {A}:\n- Step 1: Start with {A}.\n- Step 2: Using A -> BC, add B and C: {A, B, C}.\n- Step 3: Using B -> D, add D: {A, B, C, D}.\n- Step 4: Using CD -> E (since both C and D are present), add E: {A, B, C, D, E} = R.\nSince {A}+ includes all attributes of R and no proper subset of {A} can do so, {A} is a minimal candidate key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR clinical risk relation Patient_Risk(A, B, C, D, E) satisfies FDs {A -> BC, CD -> E, B -> D, E -> A}. Which attribute closure proves that {A} is a candidate key?",
        "options": [
          "A. {A}+ = {A, B}",
          "B. {A}+ = {A, C, E}",
          "C. {A}+ = {A, B, C, D, E}",
          "D. {A}+ = {A, D}"
        ],
        "correct_option": "C",
        "explanation": "{A}+ derives BC, then B derives D, then CD derives E, yielding all five attributes."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A bank credit scoring schema Credit_Model(A, B, C, D, E) has FDs {A -> BC, CD -> E, B -> D, E -> A}. Which single attribute determines the entire record and serves as a candidate key?",
        "options": [
          "A. Attribute B",
          "B. Attribute A",
          "C. Attribute C",
          "D. Attribute D"
        ],
        "correct_option": "B",
        "explanation": "Computing the attribute closure of A derives B, C, D, and E sequentially, making {A} a candidate key."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "For an online marketplace orders table R(OrderID, BuyerID, PromoCode, PaymentID) with functional dependencies OrderID -> BuyerID, PaymentID and BuyerID, PromoCode -> OrderID, what is the minimum number of candidate keys for relation R?",
        "options": [
          "A. 1 candidate key: {OrderID}",
          "B. 2 candidate keys: {OrderID, PromoCode} and {BuyerID, PromoCode}",
          "C. 3 candidate keys",
          "D. 4 candidate keys"
        ],
        "correct_option": "B",
        "explanation": "Attribute PromoCode appears on no RHS, so it must be in every key. {OrderID, PromoCode}+ = {OrderID, PromoCode, BuyerID, PaymentID} = R. {BuyerID, PromoCode}+ = {OrderID, BuyerID, PromoCode, PaymentID} = R. Thus both are minimal superkeys, giving exactly 2 candidate keys."
      }
    ]
  },
  {
    "id": "MCQ-007",
    "title": "Foreign Key Invariants on Natural Join and Cartesian Product",
    "topic": "Relational Model",
    "subtopic": "Foreign Key & Join Invariants",
    "difficulty": "Medium",
    "source": "GATE DA 2024 | Question: 26 (PYQs/DA_extracted/DA/DA2024.pdf, Page 19)",
    "source_file": "PYQs/DA_extracted/DA/DA2024.pdf",
    "source_page": 19,
    "source_qnum": "Q.26",
    "evidence_snippet": "Q.26 Consider two relations r and s defined on schemas R(A,B) and S(E,C). A is primary key of R, and E is foreign key referencing A.",
    "prompt": "Consider two relations r and s defined on schemas R(A, B) and S(A, C). A is the primary key of R, and A in S is a foreign key referencing R(A) with no NULL values. If r has m tuples and s has n tuples, what is the exact number of tuples in the natural join r ⨝ s?",
    "options": [
      "A. Exactly m tuples",
      "B. Exactly n tuples",
      "C. At most m * n tuples and at least 0 tuples",
      "D. Exactly m + n tuples"
    ],
    "correct_option": "B",
    "explanation": "Because A in S is a foreign key referencing the primary key A in R with no NULLs, every tuple in S contains an A value that exists in exactly one tuple of R (since A is the primary key of R). When computing the natural join r ⨝ s on attribute A, each of the n tuples in S joins with exactly one unique tuple in R. Thus, the natural join produces exactly n tuples.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR database, Patients(Patient_ID, Name) has m rows and Prescriptions(Patient_ID, Drug) has n rows with a valid non-null foreign key referencing Patients. What is the cardinality of Patients ⨝ Prescriptions?",
        "options": [
          "A. Exactly m tuples",
          "B. m + n tuples",
          "C. max(m, n) tuples",
          "D. Exactly n tuples"
        ],
        "correct_option": "D",
        "explanation": "Since every prescription matches exactly one patient primary key, the natural join yields exactly n rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a banking database, Accounts(Account_ID, Balance) has m tuples, and Transactions(Account_ID, Amount) has n tuples where Account_ID is a non-null foreign key referencing Accounts. How many tuples are produced by Accounts ⨝ Transactions?",
        "options": [
          "A. Exactly m tuples",
          "B. m * n tuples",
          "C. Exactly n tuples",
          "D. 0 tuples"
        ],
        "correct_option": "C",
        "explanation": "Every transaction row references exactly one primary account row, so the natural join cardinality is exactly n."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce database, Orders references Customers via foreign key CustomerID with NOT NULL constraint. Every order has a valid customer. Let n_orders be number of tuples in Orders and n_cust in Customers. What is the exact number of tuples in Orders ⨝ Customers?",
        "options": [
          "A. n_orders * n_cust",
          "B. Exactly n_orders",
          "C. Exactly n_cust",
          "D. 0 tuples"
        ],
        "correct_option": "B",
        "explanation": "Because CustomerID is a foreign key with NOT NULL and referential integrity, every order tuple matches exactly one tuple in Customers. Hence the natural join produces exactly n_orders tuples."
      }
    ]
  },
  {
    "id": "MCQ-008",
    "title": "B+ Tree Maximum Key and Pointer Capacity Calculations",
    "topic": "Indexing & Storage",
    "subtopic": "B+ Tree Fan-out & Leaf Nodes",
    "difficulty": "Medium",
    "source": "GATE DA 2024 | Question: 41 (PYQs/DA_extracted/DA/DA2024.pdf, Page 29)",
    "source_file": "PYQs/DA_extracted/DA/DA2024.pdf",
    "source_page": 29,
    "source_qnum": "Q.41",
    "evidence_snippet": "Q.41 Consider a B+ Tree where the maximum number of key values in each leaf node is 2 and the maximum number of pointers is 3.",
    "prompt": "Consider a B+ Tree where the maximum number of keys in each leaf node is 2 and the maximum number of child pointers in each internal node is 3. What is the maximum number of keys that can be stored in a B+ Tree of height 2 (where root is at height 0)?",
    "options": [
      "A. 6 keys",
      "B. 18 keys",
      "C. 27 keys",
      "D. 54 keys"
    ],
    "correct_option": "B",
    "explanation": "For a B+ tree of height 2 with root at height 0:\n- Level 0 (Root): can have at most 3 pointers to Level 1.\n- Level 1 (Internal nodes): 3 nodes, each having at most 3 pointers to Level 2 (leaf nodes) -> 3 * 3 = 9 leaf nodes.\n- Level 2 (Leaf nodes): 9 leaf nodes, each storing at most 2 keys.\n- Maximum keys = 9 * 2 = 18 keys.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A clinic triage database stores emergency patient IDs in a B+ tree of order 3 where each leaf node stores at most 2 patient keys. What is the maximum key capacity of the tree at height 2?",
        "options": [
          "A. 12 keys",
          "B. 27 keys",
          "C. 9 keys",
          "D. 18 keys"
        ],
        "correct_option": "D",
        "explanation": "Max leaf nodes = 3^2 = 9. Max keys = 9 * 2 = 18 keys."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A fintech ledger partitions micro-transaction indices using a B+ tree where internal nodes have fanout 3 and leaves hold at most 2 ledger pointers. At tree depth 2, what is the maximum number of transaction keys indexed?",
        "options": [
          "A. 9 keys",
          "B. 36 keys",
          "C. 18 keys",
          "D. 24 keys"
        ],
        "correct_option": "C",
        "explanation": "Level 0: 1 node (3 pointers). Level 1: 3 nodes (9 pointers). Level 2: 9 leaf nodes * 2 keys/leaf = 18 keys."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce SKU index, a B+ tree node fits into an 8 KB disk block. Each SKU search key takes 16 bytes and each block pointer takes 8 bytes. For an internal node of order p with (p-1) keys and p pointers: 16(p-1) + 8p <= 8192. What is the maximum order p of this internal node?",
        "options": [
          "A. 256",
          "B. 342",
          "C. 512",
          "D. 1024"
        ],
        "correct_option": "B",
        "explanation": "16p - 16 + 8p <= 8192 => 24p <= 8208 => p <= 342. Thus maximum order p = 342."
      }
    ]
  },
  {
    "id": "MCQ-009",
    "title": "SQL Correlated Subquery and Group By Aggregate Evaluation",
    "topic": "SQL & Query Processing",
    "subtopic": "Correlated Subqueries & Aggregates",
    "difficulty": "Hard",
    "source": "GATE DA 2024 | Question: 56 (PYQs/DA_extracted/DA/DA2024.pdf, Page 37)",
    "source_file": "PYQs/DA_extracted/DA/DA2024.pdf",
    "source_page": 37,
    "source_qnum": "Q.56",
    "evidence_snippet": "Q.56 Consider the following relational schema: customer(cid, cname, rating), orders(oid, cid, amount).",
    "prompt": "Consider the relation Customer(cid, cname, rating, balance). Which of the following SQL queries retrieves the names of all customers whose balance is strictly greater than the average balance of all customers having the same credit rating?",
    "options": [
      "A. SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2)",
      "B. SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2 GROUP BY C2.rating)",
      "C. SELECT C1.cname FROM Customer C1 WHERE C1.balance > AVG(C1.balance)",
      "D. SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2 WHERE C2.rating = C1.rating)"
    ],
    "correct_option": "D",
    "explanation": "To compare each customer's balance against the average balance of only those customers sharing their specific rating, a correlated subquery is required where the inner query binds `WHERE C2.rating = C1.rating`. The inner query computes the scalar average for C1's specific rating, allowing the outer query to filter customers exceeding their peer average.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital pharmacy database tracks drug inventory reorder quantities by drug category. Which query lists drugs whose reorder quantity exceeds the average reorder quantity of their category?",
        "options": [
          "A. SELECT D1.name FROM Drug D1 WHERE D1.qty > (SELECT AVG(D2.qty) FROM Drug D2)",
          "B. SELECT D1.name FROM Drug D1 WHERE D1.qty > (SELECT AVG(D2.qty) FROM Drug D2 WHERE D2.category = D1.category)",
          "C. SELECT D1.name FROM Drug D1 WHERE D1.qty > (SELECT SUM(D2.qty) FROM Drug D2)",
          "D. SELECT D1.name FROM Drug D1 WHERE D1.qty > (SELECT AVG(D2.qty) FROM Drug D2 GROUP BY D2.category)"
        ],
        "correct_option": "B",
        "explanation": "Correlating `D2.category = D1.category` calculates the average reorder quantity for D1's category."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A banking fraud engine evaluates account withdrawal amounts against peer accounts in the same risk tier. Which SQL statement correctly identifies accounts whose withdrawal exceeds the average withdrawal in their risk tier?",
        "options": [
          "A. SELECT A1.id FROM Account A1 WHERE A1.tx_amt > (SELECT AVG(A2.tx_amt) FROM Account A2 WHERE A2.risk_tier = A1.risk_tier)",
          "B. SELECT A1.id FROM Account A1 WHERE A1.tx_amt > (SELECT AVG(A2.tx_amt) FROM Account A2)",
          "C. SELECT A1.id FROM Account A1 WHERE A1.tx_amt > (SELECT MAX(A2.tx_amt) FROM Account A2)",
          "D. SELECT A1.id FROM Account A1 WHERE A1.tx_amt > AVG(A1.tx_amt)"
        ],
        "correct_option": "A",
        "explanation": "The correlated predicate `A2.risk_tier = A1.risk_tier` scopes the average calculation to the specific risk tier of account A1."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An online marketplace analyzes merchant sales with query: SELECT VendorID, AVG(ItemPrice) FROM Products P1 WHERE ItemPrice > (SELECT AVG(ItemPrice) FROM Products P2 WHERE P2.CategoryID = P1.CategoryID) GROUP BY VendorID. What does this query return?",
        "options": [
          "A. All products whose price is greater than the overall store average",
          "B. The minimum price offered by each vendor across all categories",
          "C. A list of categories having more than 5 vendors",
          "D. For each vendor, the average price of their products that are priced above the average price of their respective category"
        ],
        "correct_option": "D",
        "explanation": "The correlated subquery calculates the category average for each product's category. The outer query filters for items priced above that category average, then groups by VendorID to compute their average."
      }
    ]
  },
  {
    "id": "MCQ-010",
    "title": "Natural Join and Projection Cardinality on Three Relational Tables",
    "topic": "Relational Algebra",
    "subtopic": "Natural Join Cardinality",
    "difficulty": "Medium",
    "source": "GATE DA 2025 | Question: 17 (PYQs/DA_extracted/DA/DA2025.pdf, Page 12)",
    "source_file": "PYQs/DA_extracted/DA/DA2025.pdf",
    "source_page": 12,
    "source_qnum": "Q.17",
    "evidence_snippet": "Q.17 Consider the following three relations: Car (model, year, serial, color), Make (maker, model), Own (owner, serial).",
    "prompt": "Consider three relations: Car(model, year, serial, color), Make(maker, model), and Own(owner, serial), where serial is the primary key of Car and Own(serial) is a foreign key referencing Car. What is the effect of the relational algebra expression: π_maker(Make ⨝ (Car ⨝ Own))?",
    "options": [
      "A. Names of all car makers who produce yellow cars",
      "B. Names of all car owners who own cars of every year",
      "C. Names of all car makers whose cars are currently owned by at least one owner",
      "D. Total count of car models registered in the database"
    ],
    "correct_option": "C",
    "explanation": "The inner join Car ⨝ Own matches each car with its registered owner(s). The subsequent join with Make connects the resulting tuples with their vehicle maker via model. Finally, projecting maker (π_maker) outputs the distinct set of makers whose cars have at least one corresponding tuple in the Own relation.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR system: Vaccine(batch_no, formula, expiry), Manufacturer(mfg_name, formula), and Dose_Log(patient_id, batch_no). What does π_mfg_name(Manufacturer ⨝ (Vaccine ⨝ Dose_Log)) return?",
        "options": [
          "A. Total doses administered across all expired batches",
          "B. Formulations administered to pediatric patients exclusively",
          "C. Names of manufacturers whose vaccine formulas have been administered to at least one patient",
          "D. Patients who have received all formulas from all manufacturers"
        ],
        "correct_option": "C",
        "explanation": "The natural join chains through Dose_Log, Vaccine, and Manufacturer, and projection retrieves manufacturers with administered doses."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial securities database: Bond(isin, coupon, maturity), Issuer(institution, isin), and Portfolio(investor_id, isin). What does π_institution(Issuer ⨝ (Bond ⨝ Portfolio)) return?",
        "options": [
          "A. Total coupon payments made across all bond maturity years",
          "B. All investors who hold every bond issued by central banks",
          "C. List of all default risk ratings assigned to non-portfolio bonds",
          "D. Names of institutions whose issued bonds are held in at least one investor portfolio"
        ],
        "correct_option": "D",
        "explanation": "Joining Portfolio with Bond and Issuer filters to bonds that exist in a portfolio, and projecting institution yields active bond issuers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce database has three relations: Order_Items(Item_ID, SKU, Order_ID), Products(SKU, Brand_ID), and Brands(Brand_ID, Brand_Name). What is the result of ∏_Brand_Name (Order_Items ⨝ Products ⨝ Brands)?",
        "options": [
          "A. The names of all brands registered in the product catalog regardless of whether they have any orders",
          "B. The total number of items ordered per brand",
          "C. The distinct names of brands whose products have been ordered in at least one order",
          "D. The Cartesian product of all ordered items and brands"
        ],
        "correct_option": "C",
        "explanation": "The natural join joins Order_Items with Products on SKU, and then with Brands on Brand_ID. Projecting Brand_Name yields the set of brand names that appear in at least one order."
      }
    ]
  },
  {
    "id": "MCQ-011",
    "title": "Referential Integrity Cascading Deletions on Foreign Keys",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "Foreign Key ON DELETE CASCADE",
    "difficulty": "Medium",
    "source": "GATE DA 2025 | Question: 56 (PYQs/DA_extracted/DA/DA2025.pdf, Page 30)",
    "source_file": "PYQs/DA_extracted/DA/DA2025.pdf",
    "source_page": 30,
    "source_qnum": "Q.56",
    "evidence_snippet": "Q. 56 Consider the following two relations, named Customer and Person, in a database: Person (aadhaar CHAR(12) PRIMARY KEY, name VARCHAR(32)); Customer (name VARCHAR(32), email VARCHAR(32) PRIMARY KEY, phone CHAR(10), aadhaar CHAR(12), FOREIGN KEY (aadhaar) REFERENCES Person(aadhaar) ON DELETE CASCADE);",
    "prompt": "Consider two relations Person(aadhaar PRIMARY KEY, name) and Customer(email PRIMARY KEY, name, phone, aadhaar FOREIGN KEY REFERENCES Person(aadhaar) ON DELETE CASCADE). If a tuple is deleted from Person, what happens in Customer?",
    "options": [
      "A. Deletion is rejected and aborted by the database engine",
      "B. All tuples in Customer referencing the deleted aadhaar are set to NULL",
      "C. All tuples in Customer referencing the deleted aadhaar are automatically deleted",
      "D. Only the first matching tuple in Customer is deleted"
    ],
    "correct_option": "C",
    "explanation": "Under the ON DELETE CASCADE referential integrity action, when a parent tuple in Person is deleted, the database management system automatically deletes all referencing child tuples in Customer that match the parent primary key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical trial database: Subject(subject_id PRIMARY KEY, birth_year) and Biometric_Sample(sample_barcode PRIMARY KEY, subject_id FOREIGN KEY REFERENCES Subject(subject_id) ON DELETE CASCADE). If a patient withdraws consent and their record in Subject is purged, how are their biometric samples treated?",
        "options": [
          "A. All biometric sample rows linked to the withdrawn subject are automatically cascaded and removed",
          "B. The delete operation fails and requests admin override",
          "C. Biometric samples are anonymized by nullifying the subject_id column",
          "D. Only samples collected within the last 30 days are removed"
        ],
        "correct_option": "A",
        "explanation": "ON DELETE CASCADE automatically purges all child sample records referencing the deleted subject."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an investment banking ledger: Corporate_Entity(lei PRIMARY KEY, legal_name) and Trading_Account(acc_no PRIMARY KEY, lei FOREIGN KEY REFERENCES Corporate_Entity(lei) ON DELETE CASCADE). When a corporate entity is dissolved and deleted from the database, what occurs to its associated trading accounts?",
        "options": [
          "A. The transaction rolls back due to a constraint violation error",
          "B. Foreign keys in all trading accounts are overwritten with zero",
          "C. Accounts remain active but are detached into an orphan table",
          "D. All associated trading accounts are automatically purged from Trading_Account by the DBMS"
        ],
        "correct_option": "D",
        "explanation": "ON DELETE CASCADE causes all dependent trading accounts matching the deleted LEI to be cascaded and deleted automatically."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a marketplace schema, Order_Items defines a foreign key referencing Orders(OrderID) with ON DELETE CASCADE. If a customer cancels an order and the corresponding tuple in Orders is deleted, what happens to the rows in Order_Items?",
        "options": [
          "A. The delete operation is rejected with a referential integrity violation error",
          "B. The foreign key values in Order_Items are set to NULL",
          "C. All corresponding rows in Order_Items are automatically deleted by the database engine",
          "D. The Order_Items rows are moved into a separate archive table"
        ],
        "correct_option": "C",
        "explanation": "ON DELETE CASCADE specifies that when a referenced parent row is deleted, all dependent child rows in the referencing table are automatically deleted."
      }
    ]
  },
  {
    "id": "MCQ-012",
    "title": "Candidate Key Derivation from Functional Dependencies",
    "topic": "Functional Dependencies",
    "subtopic": "Candidate Key Computation",
    "difficulty": "Medium",
    "source": "GATE DA 2025 | Question: 57 (PYQs/DA_extracted/DA/DA2025.pdf, Page 31)",
    "source_file": "PYQs/DA_extracted/DA/DA2025.pdf",
    "source_page": 31,
    "source_qnum": "Q.57",
    "evidence_snippet": "Q. 57 Consider a database relation R with attributes ABCDEFG, and having the following functional dependencies: A → BCEF, E → DG, BC → A. Which of the following statements is/are correct?",
    "prompt": "Consider relation R(A, B, C, D, E, F, G) with functional dependencies: A -> BCEF, E -> DG, and BC -> A. Which of the following sets contains all candidate keys of R?",
    "options": [
      "A. {A, BC}",
      "B. {A, E}",
      "C. {BC, DG}",
      "D. {A, BC, E}"
    ],
    "correct_option": "A",
    "explanation": "Compute attribute closures:\n- A+ = {A, B, C, E, F} U {D, G} = {A, B, C, D, E, F, G} (All attributes, so A is a candidate key).\n- (BC)+ = {B, C} U {A} = A+ = {A, B, C, D, E, F, G} (BC is a candidate key).\n- E+ = {E, D, G} (cannot determine A, B, C, F).\nHence, {A, BC} are the only candidate keys of R.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An ICU telemetry schema Patient_Sensor(A, B, C, D, E, F, G) has FDs: A -> BCEF, E -> DG, and BC -> A. Which minimal attribute sets serve as unique candidate identifiers for sensor telemetry records?",
        "options": [
          "A. Only {E} and {DG}",
          "B. All attributes ABCDEFG together",
          "C. Either {A} or {BC}",
          "D. Only {BC} without {A}"
        ],
        "correct_option": "C",
        "explanation": "Both A+ and (BC)+ compute the complete schema closure ABCDEFG, establishing {A} and {BC} as candidate keys."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A credit assessment schema Risk_Model(A, B, C, D, E, F, G) defines dependencies: A -> BCEF, E -> DG, BC -> A. Which attribute combinations can uniquely identify every corporate entity in the assessment model?",
        "options": [
          "A. Only {E} combined with {DG}",
          "B. Either {A} alone or {BC} composite",
          "C. Every singleton attribute in the schema",
          "D. {A, B, C, D} together as a composite key"
        ],
        "correct_option": "B",
        "explanation": "A+ and (BC)+ both determine all 7 attributes, making {A} and {BC} the minimal candidate keys."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "For an e-commerce payment settlement relation Settlement(P, Q, R, S, T) with functional dependencies P -> Q, Q -> R, R -> S, S -> T, and T -> P, which of the following is TRUE?",
        "options": [
          "A. Each of P, Q, R, S, and T is individually a candidate key",
          "B. Only {P, Q} together form a candidate key",
          "C. The relation has no candidate keys",
          "D. Only {P} is a candidate key"
        ],
        "correct_option": "A",
        "explanation": "Because the dependencies form a complete cycle P -> Q -> R -> S -> T -> P, the attribute closure of each individual single attribute includes all five attributes. Thus P, Q, R, S, and T are each individual candidate keys."
      }
    ]
  },
  {
    "id": "MCQ-013",
    "title": "Minimal Candidate Key Identification with Extraneous Attributes",
    "topic": "Functional Dependencies",
    "subtopic": "Candidate Key Computation",
    "difficulty": "Medium",
    "source": "GATE DA 2026 | Question: 17 (PYQs/DA_extracted/DA/DA2026.pdf, Page 12)",
    "source_file": "PYQs/DA_extracted/DA/DA2026.pdf",
    "source_page": 12,
    "source_qnum": "Q.17",
    "evidence_snippet": "Q.17 Let R(A,B,C,D,E) be a relational schema with functional dependency set F={ABC, CDE, EA}. Which of the following statements is correct? (A) AD, ED and CD are the only candidate keys of R.",
    "prompt": "Let R(A, B, C, D, E) be a relational schema with functional dependencies F = {A -> BC, CD -> E, E -> A}. Which of the following statements is correct?",
    "options": [
      "A. AD, ED and CD are the only candidate keys of R",
      "B. AD and ED are the only candidate keys of R",
      "C. A, E and CD are the only candidate keys of R",
      "D. CD is the only candidate key of R"
    ],
    "correct_option": "A",
    "explanation": "Note that attribute D does not appear on the right-hand side of any dependency, so D must be present in every candidate key.\n- (AD)+ = {A, D} -> {B, C, D} -> {E} = {A, B, C, D, E}\n- (ED)+ = {E, D} -> {A, D} -> {B, C, D} = {A, B, C, D, E}\n- (CD)+ = {C, D} -> {E} -> {A} -> {B, C} = {A, B, C, D, E}\nThus AD, ED, and CD are all minimal superkeys, i.e., the only candidate keys of R.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a multi-ward hospital scheduling system R(A, B, C, D, E) with F = {A -> BC, CD -> E, E -> A}, where D represents medical department, what are all the candidate keys?",
        "options": [
          "A. Only ED and CD",
          "B. A, B, and C",
          "C. AD, ED, and CD only",
          "D. Only AD alone"
        ],
        "correct_option": "C",
        "explanation": "D cannot be derived from any RHS; appending D to A, E, and C produces full closures for AD, ED, and CD."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated equity order router with schema R(A, B, C, D, E) and F = {A -> BC, CD -> E, E -> A}, where D is trading desk ID, which combinations serve as candidate keys?",
        "options": [
          "A. Only AD and ED",
          "B. AD, ED, and CD only",
          "C. Only CD alone",
          "D. A, E, and CD"
        ],
        "correct_option": "B",
        "explanation": "Attribute D is essential; testing closures shows (AD)+, (ED)+, and (CD)+ each yield ABCDE."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce vendor rating table has schema Vendor_Review(V, R, C, D) with FDs VR -> C and C -> D. A developer proposes {V, R, C} as a candidate key. Is this proposal correct?",
        "options": [
          "A. No, because {V, R, C} is a superkey but not minimal since {V, R} alone determines all attributes",
          "B. Yes, because {V, R, C} contains three attributes",
          "C. Yes, because C determines D",
          "D. No, because Candidate Keys can only have 1 attribute"
        ],
        "correct_option": "A",
        "explanation": "{V, R}+ = {V, R, C, D}. Because {V, R} is already a superkey, proper superset {V, R, C} is extraneous and not minimal. A candidate key must be a minimal superkey."
      }
    ]
  },
  {
    "id": "MCQ-014",
    "title": "Operations Preserving Referential Integrity Invariants",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "Foreign Key Modification Safety",
    "difficulty": "Easy",
    "source": "GATE DA 2026 | Question: 26 (PYQs/DA_extracted/DA/DA2026.pdf, Page 18)",
    "source_file": "PYQs/DA_extracted/DA/DA2026.pdf",
    "source_page": 18,
    "source_qnum": "Q.26",
    "evidence_snippet": "Q.26 Consider two relations r and s defined on the relational schemas R(A,B) and S(E,C), respectively. A is the primary key of R and E is a foreign key of S referencing A in R. Which of the following operations will NEVER violate the foreign key constraint? (A) Inserting records into relation r (B) Deleting records from relation s",
    "prompt": "Consider relations r and s on schemas R(A, B) and S(E, C) where A is the primary key of R and E is a foreign key of S referencing A in R. Which pair of operations will NEVER violate the foreign key constraint?",
    "options": [
      "A. Inserting records into relation r, and deleting records from relation s",
      "B. Deleting records from relation r, and inserting records into relation s",
      "C. Updating attribute A in relation r, and updating attribute E in relation s",
      "D. Deleting records from relation r, and deleting records from relation s"
    ],
    "correct_option": "A",
    "explanation": "A foreign key constraint requires that every value of E in s must appear in A in r.\n- Inserting into r (parent table) adds valid keys, which can never create dangling references in s.\n- Deleting from s (child table) removes a referencing tuple, which can never violate referential integrity.\nConversely, deleting from r or inserting into s could introduce dangling references.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an outpatient clinic EHR with Doctors(doc_id PK) and Appointments(appt_id PK, doc_id FK referencing Doctors): which operations are guaranteed never to violate referential integrity?",
        "options": [
          "A. Terminating a doctor record from Doctors, and booking an appointment in Appointments",
          "B. Editing doc_id in Doctors while active appointments refer to it",
          "C. Onboarding a new doctor in Doctors, and canceling an appointment from Appointments",
          "D. Mass-deleting doctor profiles during open clinic hours"
        ],
        "correct_option": "C",
        "explanation": "Inserting parent doctor records and deleting child appointments never produce dangling foreign keys."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a merchant payment system with Accounts(acc_id PK) and Transactions(tx_id PK, acc_id FK referencing Accounts): which operations can NEVER violate the foreign key integrity constraint?",
        "options": [
          "A. Deleting an account from Accounts, and inserting an unverified transaction into Transactions",
          "B. Creating a new merchant account in Accounts, and purging an archived transaction from Transactions",
          "C. Modifying account IDs in Accounts without cascading",
          "D. Inserting new records into Transactions with arbitrary account IDs"
        ],
        "correct_option": "B",
        "explanation": "Adding parent accounts and deleting child transactions can never cause dangling references."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce platform with parent table Categories(CatID, CatName) and child table Products(ProdID, CatID, Price) where CatID is a foreign key, which of the following operations can NEVER violate referential integrity?",
        "options": [
          "A. Inserting a new tuple into Categories, and deleting an existing tuple from Products",
          "B. Deleting a tuple from Categories, and inserting a tuple into Products",
          "C. Updating CatID in Categories, and inserting a tuple into Products",
          "D. Deleting a tuple from Categories, and updating CatID in Products"
        ],
        "correct_option": "A",
        "explanation": "Inserting into the parent table (Categories) cannot create a dangling foreign key. Deleting from the child table (Products) removes references without affecting the parent. Thus neither operation can ever violate referential integrity."
      }
    ]
  },
  {
    "id": "MCQ-015",
    "title": "B+ Tree Node Split and Key Promotion on Insertion",
    "topic": "Indexing & Storage",
    "subtopic": "B+ Tree Insertion and Splitting",
    "difficulty": "Hard",
    "source": "GATE DA 2026 | Question: 41 (PYQs/DA_extracted/DA/DA2026.pdf, Page 26)",
    "source_file": "PYQs/DA_extracted/DA/DA2026.pdf",
    "source_page": 26,
    "source_qnum": "Q.41",
    "evidence_snippet": "Q.41 Consider a B+ Tree where the maximum number of key values in each leaf node is 2 and the maximum number of pointers in each non-leaf node is 3. Let the content of the B+ Tree be as shown in the figure. Which of the following options denotes the key value(s) stored in the root node after inserting a key value 3 in the given B+ Tree? (A) 5 (B) 8",
    "prompt": "Consider a B+ Tree where leaf nodes hold at most 2 keys and internal nodes hold at most 3 pointers (order 3). Initially, the tree contains leaf [1, 2] and [5, 8] with root containing key 5. Upon inserting key 3 into the leftmost leaf [1, 2], the leaf overflows to [1, 2, 3] and splits. What key(s) are stored in the root node after rebalancing?",
    "options": [
      "A. 3, 5",
      "B. 5",
      "C. 2, 5",
      "D. 3"
    ],
    "correct_option": "A",
    "explanation": "When key 3 is inserted into the leaf [1, 2], the leaf overflows with keys [1, 2, 3]. It splits into left leaf [1, 2] and right leaf [3], promoting the copy of key 3 to the parent root node. Since the root previously held key 5 and had capacity for 2 keys (up to 3 child pointers), it now holds keys [3, 5] without overflowing.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An emergency triage B+ tree indexes patient urgency scores. Leaf capacity is 2; root holds key 5. Inserting triage priority 3 into leaf [1, 2] causes a split. What keys are present in the root node?",
        "options": [
          "A. 1, 3",
          "B. 5 alone",
          "C. 3, 5",
          "D. 2, 5"
        ],
        "correct_option": "C",
        "explanation": "Splitting [1, 2, 3] promotes key 3 into the root alongside key 5, yielding [3, 5]."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A banking ledger indexes transaction sequence numbers in an order-3 B+ tree. Leaves store up to 2 keys; root currently holds key 5 with children pointing to leaves [1, 2] and [5, 8]. After transaction sequence 3 is committed and inserted, what keys reside in the root?",
        "options": [
          "A. 2, 5",
          "B. 3, 5",
          "C. 5, 8",
          "D. 3 alone"
        ],
        "correct_option": "B",
        "explanation": "The left leaf splits on inserting 3, promoting 3 to join 5 in the root node, resulting in [3, 5]."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a B+ tree index on product SKU_Price where leaf nodes have maximum capacity of 3 keys, inserting a 4th key into a full leaf node causes a node split. In a B+ tree, how is the split key handled between leaf and parent?",
        "options": [
          "A. The median key is copied into the parent internal node while also being retained in the right leaf node",
          "B. The median key is deleted from the tree entirely",
          "C. The median key is moved to the parent and removed from the leaf node (like in a B-tree)",
          "D. Both sibling leaf nodes are merged into the root"
        ],
        "correct_option": "A",
        "explanation": "In a B+ tree, all data records and search keys must reside in the leaf nodes. Therefore, during a leaf split, the split key is copied (duplicated) into the parent internal node and retained in the leaf."
      }
    ]
  },
  {
    "id": "MCQ-016",
    "title": "Natural Join Tuple Cardinality Across Three Relations",
    "topic": "Relational Algebra",
    "subtopic": "Multi-Table Natural Join",
    "difficulty": "Medium",
    "source": "GATE DA 2026 | Question: 42 (PYQs/DA_extracted/DA/DA2026.pdf, Page 27)",
    "source_file": "PYQs/DA_extracted/DA/DA2026.pdf",
    "source_page": 27,
    "source_qnum": "Q.42",
    "evidence_snippet": "Q.42 Consider the given relations 𝑋, 𝑌 and 𝑍. The relation 𝑋 has three columns 𝑃, 𝑄 and 𝑅. The relation 𝑌 has three columns 𝑃, 𝑄 and 𝑆. The relation 𝑍 has two columns 𝑃 and 𝑇.",
    "prompt": "Consider relations X(P, Q, R), Y(P, Q, S), and Z(P, T). Suppose X has tuples {(1, 2, 'a'), (1, 3, 'b')}, Y has tuples {(1, 2, 'c'), (1, 4, 'd')}, and Z has tuples {(1, 'e'), (2, 'f')}. How many tuples are present in the natural join X ⨝ Y ⨝ Z?",
    "options": [
      "A. 1",
      "B. 2",
      "C. 0",
      "D. 4"
    ],
    "correct_option": "A",
    "explanation": "1. Compute X ⨝ Y on common attributes (P, Q):\n- Tuple (1, 2, 'a') in X matches (1, 2, 'c') in Y because both have P=1, Q=2. Output: (1, 2, 'a', 'c').\n- Tuples with Q=3 and Q=4 have no match.\n2. Compute (X ⨝ Y) ⨝ Z on common attribute P:\n- The tuple (1, 2, 'a', 'c') has P=1, which matches (1, 'e') in Z.\n- Output: (1, 2, 'a', 'c', 'e').\nTotal tuple count is exactly 1.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical trials registry: Protocol(P, Q, R), Trial_Site(P, Q, S), and Drug(P, T) where P is trial_id and Q is phase_id. If only a single matching (trial_id, phase_id) combination is common to Protocol, Trial_Site, and Drug, how many tuples are in Protocol ⨝ Trial_Site ⨝ Drug?",
        "options": [
          "A. 3 tuples",
          "B. 0 tuples",
          "C. Exactly 1 tuple",
          "D. 2 tuples"
        ],
        "correct_option": "C",
        "explanation": "Natural join filters out non-matching Q values and retains only the single tuple satisfying all join equality constraints."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an algorithmic trading warehouse: Quotes(P, Q, R), Trades(P, Q, S), and Assets(P, T) where P is asset_id and Q is exchange_id. If only one (asset_id, exchange_id) pair exists across all three relations, how many rows result from Quotes ⨝ Trades ⨝ Assets?",
        "options": [
          "A. 2 rows",
          "B. Exactly 1 row",
          "C. 0 rows",
          "D. 4 rows"
        ],
        "correct_option": "B",
        "explanation": "Matching on (P, Q) between Quotes and Trades produces 1 intermediate row, which then matches 1 row in Assets on P."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Consider relations Cart(User_ID, Cart_ID) with 10 tuples, Cart_Items(Cart_ID, Item_ID) with 20 tuples, and Inventory(Item_ID, Stock) with 50 tuples. If Cart_ID is foreign key in Cart_Items referencing Cart, and Item_ID in Cart_Items references Inventory, what is the exact number of tuples in Cart ⨝ Cart_Items ⨝ Inventory?",
        "options": [
          "A. Exactly 20 tuples",
          "B. 1000 tuples",
          "C. 10 tuples",
          "D. 50 tuples"
        ],
        "correct_option": "A",
        "explanation": "Every item in Cart_Items (20 tuples) references exactly one valid Cart and one valid Inventory item. Hence each Cart_Items tuple joins with exactly one Cart tuple and one Inventory tuple, yielding exactly 20 tuples."
      }
    ]
  },
  {
    "id": "MCQ-017",
    "title": "SQL Correlated Subquery and Windowing for Group Cardinality",
    "topic": "SQL & Query Processing",
    "subtopic": "Group Size Aggregation via Subquery",
    "difficulty": "Medium",
    "source": "GATE DA 2026 | Question: 51 (PYQs/DA_extracted/DA/DA2026.pdf, Page 34)",
    "source_file": "PYQs/DA_extracted/DA/DA2026.pdf",
    "source_page": 34,
    "source_qnum": "Q.51",
    "evidence_snippet": "Q.51 Consider a table Employee(EmpID, TeamID), where the column EmpID (ID of an employee) is the primary key. The column TeamID denotes the team ID of the team of which the employee is a member. TeamID is a NOT NULL column. We want to display the size of the team (denoted as TeamSize) in which each employee is a member by using SQL.",
    "prompt": "Consider table Employee(EmpID PK, TeamID NOT NULL). To display each employee's EmpID alongside the size of their team (TeamSize), which of the following SQL queries is correct?",
    "options": [
      "A. SELECT EmpID, (SELECT COUNT(*) FROM Employee E2 WHERE E2.TeamID = E1.TeamID) AS TeamSize FROM Employee E1",
      "B. SELECT EmpID, COUNT(TeamID) AS TeamSize FROM Employee GROUP BY EmpID",
      "C. SELECT EmpID, COUNT(*) AS TeamSize FROM Employee GROUP BY TeamID",
      "D. SELECT EmpID, SUM(TeamID) AS TeamSize FROM Employee"
    ],
    "correct_option": "A",
    "explanation": "Query (A) uses a correlated scalar subquery `(SELECT COUNT(*) FROM Employee E2 WHERE E2.TeamID = E1.TeamID)` in the SELECT clause, which computes the total member count for the specific team of employee E1 while retaining all individual employee rows. Query (B) groups by EmpID (giving TeamSize=1 for all), while (C) fails because EmpID is not in the GROUP BY clause.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital staff roster Nurses(NurseID PK, WardID NOT NULL), which SQL query displays each nurse's NurseID along with the total count of nurses assigned to their ward?",
        "options": [
          "A. SELECT NurseID, COUNT(*) FROM Nurses GROUP BY NurseID",
          "B. SELECT WardID, COUNT(NurseID) FROM Nurses",
          "C. SELECT NurseID, (SELECT COUNT(*) FROM Nurses N2 WHERE N2.WardID = N1.WardID) AS WardStaffCount FROM Nurses N1",
          "D. SELECT NurseID, MAX(WardID) FROM Nurses GROUP BY WardID"
        ],
        "correct_option": "C",
        "explanation": "Correlating `N2.WardID = N1.WardID` inside the projection computes the size of each nurse's ward while listing each nurse."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an investment bank portfolio table Positions(PositionID PK, DeskID NOT NULL), which SQL query lists each PositionID alongside the total number of positions managed by that desk?",
        "options": [
          "A. SELECT PositionID, COUNT(*) FROM Positions GROUP BY DeskID",
          "B. SELECT PositionID, (SELECT COUNT(*) FROM Positions P2 WHERE P2.DeskID = P1.DeskID) AS DeskSize FROM Positions P1",
          "C. SELECT PositionID, COUNT(DeskID) FROM Positions GROUP BY PositionID",
          "D. SELECT PositionID, AVG(DeskID) FROM Positions"
        ],
        "correct_option": "B",
        "explanation": "The correlated subquery counts rows sharing the outer desk ID without collapsing individual position rows."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An online marketplace runs query: SELECT P.Category, P.ProductName, P.Price FROM Products P WHERE P.Price = (SELECT MAX(P2.Price) FROM Products P2 WHERE P2.Category = P.Category). What does this query produce?",
        "options": [
          "A. The most expensive product(s) within each category",
          "B. The overall highest priced product in the entire store",
          "C. Products whose price equals the category average price",
          "D. The category name with the highest total revenue"
        ],
        "correct_option": "A",
        "explanation": "The correlated subquery finds the maximum price for the category of the current product P. The outer query retains products whose price matches that category maximum."
      }
    ]
  },
  {
    "id": "MCQ-018",
    "title": "Dependency Preservation in 3NF and BCNF Decompositions",
    "topic": "Normalization & Functional Dependencies",
    "subtopic": "Dependency Preservation & Normal Forms",
    "difficulty": "Medium",
    "source": "GATE CSE 2026 Set 1 | Question: 31 (PYQs/CS_extracted/CS/2026_CS1.pdf, Page 23)",
    "source_file": "PYQs/CS_extracted/CS/2026_CS1.pdf",
    "source_page": 23,
    "source_qnum": "Q.31",
    "evidence_snippet": "Q.31 In the context of relational database normalization, which of the following statements is/are true? (A) It is always possible to obtain a dependency-preserving 3NF decomposition of a relation (B) It is always possible to obtain a dependency-preserving 1NF decomposition of a relation",
    "prompt": "In the context of relational database schema normalization, which of the following statements is ALWAYS TRUE?",
    "options": [
      "A. It is always possible to obtain a lossless-join, dependency-preserving decomposition into 3NF",
      "B. It is always possible to obtain a lossless-join, dependency-preserving decomposition into BCNF",
      "C. Any relation with only prime attributes is in BCNF",
      "D. Lossless join decomposition is not guaranteed for 3NF"
    ],
    "correct_option": "A",
    "explanation": "Using the 3NF synthesis algorithm (based on a minimal cover of functional dependencies), it is ALWAYS possible to achieve a decomposition that is simultaneously lossless-join and dependency-preserving. In contrast, BCNF guarantees lossless-join but does NOT always preserve functional dependencies.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital health records architect decomposes medical charts to minimize data redundancy. Which property can always be guaranteed when decomposing into 3NF?",
        "options": [
          "A. BCNF guarantees dependency preservation for all clinical relationships",
          "B. Medical charts with composite primary keys are automatically in 4NF",
          "C. The decomposition can always be both lossless-join and dependency-preserving",
          "D. 3NF permits transitive dependencies among non-prime attributes"
        ],
        "correct_option": "C",
        "explanation": "A dependency-preserving lossless-join decomposition into 3NF is always achievable via standard synthesis."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When normalizing a banking core transaction ledger to eliminate update anomalies while preserving auditing rules, which theoretical guarantee holds?",
        "options": [
          "A. BCNF decomposition is always guaranteed to preserve all transaction dependencies",
          "B. A lossless-join, dependency-preserving decomposition is always achievable in 3NF",
          "C. 3NF decomposition requires discarding functional dependency verification",
          "D. 2NF guarantees complete elimination of redundancy across all audit tables"
        ],
        "correct_option": "B",
        "explanation": "3NF synthesis guarantees both lossless-join and dependency preservation; BCNF cannot always preserve dependencies."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When decomposing an e-commerce checkout schema R with functional dependencies F to eliminate redundancy, which statement is always GUARANTEED in relational database theory?",
        "options": [
          "A. A lossless-join, dependency-preserving decomposition into 3NF is always achievable",
          "B. A lossless-join, dependency-preserving decomposition into BCNF is always achievable",
          "C. BCNF decomposition always preserves all functional dependencies",
          "D. 3NF decomposition can never achieve a lossless join"
        ],
        "correct_option": "A",
        "explanation": "Bernstein's 3NF synthesis algorithm guarantees both a lossless join and dependency preservation. In contrast, BCNF decomposition guarantees lossless join, but cannot always preserve all functional dependencies."
      }
    ]
  },
  {
    "id": "MCQ-019",
    "title": "Tuple Relational Calculus Equivalence to Relational Algebra Join",
    "topic": "Relational Calculus",
    "subtopic": "TRC to Relational Algebra Translation",
    "difficulty": "Hard",
    "source": "GATE CSE 2026 Set 1 | Question: 43 (PYQs/CS_extracted/CS/2026_CS1.pdf, Page 32)",
    "source_file": "PYQs/CS_extracted/CS/2026_CS1.pdf",
    "source_page": 32,
    "source_qnum": "Q.43",
    "evidence_snippet": "Q.43 Consider a relational database schema with two relations 𝑅(𝑃, 𝑄) and 𝑆(𝑋, 𝑌). Let  𝐸 = {⟨𝑢⟩∣∃𝑣 ∃𝑤  ⟨𝑢, 𝑣⟩∈𝑅 ∧ ⟨𝑣, 𝑤⟩ ∈𝑆}  be a tuple relational calculus expression. Which one of the following relational algebraic expressions is equivalent to 𝐸 ?",
    "prompt": "Consider relations R(P, Q) and S(X, Y). Let E = { ⟨u⟩ | ∃v ∃w ( ⟨u, v⟩ ∈ R ∧ ⟨v, w⟩ ∈ S ) } be a tuple relational calculus expression. Which relational algebra expression is equivalent to E?",
    "options": [
      "A. ∏_P ( R ⨝_{R.Q = S.X} S )",
      "B. ∏_P ( R ⨝_{R.P = S.X} S )",
      "C. ∏_Q ( R ⨝_{R.Q = S.Y} S )",
      "D. ∏_X ( R ⨝_{R.P = S.Y} S )"
    ],
    "correct_option": "A",
    "explanation": "In the expression E = { ⟨u⟩ | ∃v ∃w ( ⟨u, v⟩ ∈ R ∧ ⟨v, w⟩ ∈ S ) }:\n- ⟨u, v⟩ ∈ R implies attribute P = u and attribute Q = v.\n- ⟨v, w⟩ ∈ S implies attribute X = v and attribute Y = w.\nSince the shared variable v equates R.Q and S.X (R.Q = S.X), this represents an equijoin R ⨝_{R.Q = S.X} S. The free variable is u, which corresponds to attribute P. Thus, projecting P yields ∏_P ( R ⨝_{R.Q = S.X} S ).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an oncology registry with Patients(PatientId, TrialCode) and Trials(TrialCode, Drug), the TRC query is { ⟨u⟩ | ∃v ∃w ( ⟨u, v⟩ ∈ Patients ∧ ⟨v, w⟩ ∈ Trials ) }. Which relational algebra expression computes this set?",
        "options": [
          "A. ∏_Drug ( Patients ⨝ Trials )",
          "B. ∏_PatientId ( Patients ⨝_{Patients.PatientId = Trials.TrialCode} Trials )",
          "C. ∏_PatientId ( Patients ⨝_{Patients.TrialCode = Trials.TrialCode} Trials )",
          "D. ∏_TrialCode ( Patients ⨝ Trials )"
        ],
        "correct_option": "C",
        "explanation": "Equijoining on TrialCode and projecting PatientId implements the exact semantics of the TRC expression."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial securities system with Orders(OrderId, SecurityId) and SecInfo(SecurityId, Sector), the TRC query retrieves OrderIds whose SecurityId appears in SecInfo: { ⟨u⟩ | ∃v ∃w ( ⟨u, v⟩ ∈ Orders ∧ ⟨v, w⟩ ∈ SecInfo ) }. What is the equivalent relational algebra query?",
        "options": [
          "A. ∏_Sector ( Orders ⨝ SecInfo )",
          "B. ∏_OrderId ( Orders ⨝_{Orders.SecurityId = SecInfo.SecurityId} SecInfo )",
          "C. ∏_OrderId ( Orders ⨝_{Orders.OrderId = SecInfo.SecurityId} SecInfo )",
          "D. ∏_SecurityId ( Orders ⨝ SecInfo )"
        ],
        "correct_option": "B",
        "explanation": "Matching on the second attribute of Orders and first of SecInfo equates SecurityId, and projecting the first attribute outputs OrderId."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce platform with relations Orders(OrderID, CustID, Total) and Customers(CustID, Name, Country), which Tuple Relational Calculus (TRC) formula is equivalent to ∏_OrderID (Orders ⨝_{Orders.CustID = Customers.CustID} Customers)?",
        "options": [
          "A. { t | ∃o ∈ Orders ∃c ∈ Customers (t[OrderID] = o[OrderID] ∧ o[CustID] = c[CustID]) }",
          "B. { t | ∀o ∈ Orders ∃c ∈ Customers (o[Total] > 0) }",
          "C. { t | ∃c ∈ Customers (c[Country] = 'USA') }",
          "D. { t | ∀c ∈ Customers (t[CustID] = c[CustID]) }"
        ],
        "correct_option": "A",
        "explanation": "The TRC formula asserts existential quantification of tuple o in Orders and c in Customers with matching join attribute CustID, projecting OrderID."
      }
    ]
  },
  {
    "id": "MCQ-020",
    "title": "Armstrong Axioms: Derivation of the Union Rule",
    "topic": "Functional Dependencies",
    "subtopic": "Inference Rules & Axioms",
    "difficulty": "Medium",
    "source": "GATE CSE 2026 Set 2 | Question: 42 (PYQs/CS_extracted/CS/2026_CS2.pdf, Page 29)",
    "source_file": "PYQs/CS_extracted/CS/2026_CS2.pdf",
    "source_page": 29,
    "source_qnum": "Q.42",
    "evidence_snippet": "Q.42 In the context of schema normalization in relational DBMS, consider a set F of functional dependencies. The three rules of Armstrong’s Axioms are Reflexivity, Augmentation, and Transitivity. The additional rule of Union is defined as follows.",
    "prompt": "According to Armstrong's Axioms (Reflexivity, Augmentation, Transitivity), how is the Union Rule ('If X -> Y and X -> Z, then X -> YZ') formally derived?",
    "options": [
      "A. By augmenting X -> Y with X to get X -> XY, augmenting X -> Z with Y to get XY -> YZ, and applying Transitivity to yield X -> YZ",
      "B. By taking the intersection of attribute closures of Y and Z",
      "C. By applying Reflexivity directly on attribute set YZ",
      "D. By decomposing X into disjoint subsets and applying Augmentation"
    ],
    "correct_option": "A",
    "explanation": "Proof of Union Rule from Armstrong's Axioms:\n1. Given X -> Y, augment with X: XX -> XY, so X -> XY.\n2. Given X -> Z, augment with Y: XY -> YZ.\n3. By transitivity: from X -> XY and XY -> YZ, we derive X -> YZ.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical EHR data model proof: given PatientID -> BloodGroup and PatientID -> RhFactor, what sequence of Armstrong's axioms derives PatientID -> BloodGroup RhFactor?",
        "options": [
          "A. Invert the dependencies and apply Reflexivity",
          "B. Compute the join of BloodGroup and RhFactor",
          "C. Augment PatientID -> BloodGroup with PatientID, augment PatientID -> RhFactor with BloodGroup, and apply Transitivity",
          "D. Apply Pseudo-transitivity directly without augmentation"
        ],
        "correct_option": "C",
        "explanation": "The Union inference rule is strictly derived via Augmentation followed by Transitivity."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking compliance engine proving dependency validity: given Account -> Holder and Account -> Balance, how is Account -> Holder Balance proven using primary axioms?",
        "options": [
          "A. Intersect the primary keys of Holder and Balance",
          "B. Augment Account -> Holder with Account, augment Account -> Balance with Holder, then apply Transitivity",
          "C. Decompose Account into Holder and apply Reflexivity",
          "D. Apply Decomposition directly to Account"
        ],
        "correct_option": "B",
        "explanation": "Augmenting X->Y to X->XY, augmenting X->Z to XY->YZ, and applying Transitivity proves the Union rule."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce product schema with FDs X -> Y and X -> Z, which sequence of Armstrong's axioms formally derives the Union Rule X -> YZ?",
        "options": [
          "A. Augment X -> Y with X to get X -> XY; augment X -> Z with Y to get XY -> YZ; apply Transitivity to obtain X -> YZ",
          "B. Apply Decomposition followed by Reflexivity",
          "C. Apply Reflexivity directly to Z",
          "D. Apply Pseudo-transitivity without augmentation"
        ],
        "correct_option": "A",
        "explanation": "Augmentation of X -> Y with X yields X -> XY (since XX = X). Augmentation of X -> Z with Y yields XY -> YZ. By transitivity, X -> XY and XY -> YZ yield X -> YZ."
      }
    ]
  },
  {
    "id": "MCQ-021",
    "title": "ACID Properties: Transaction Durability Definition",
    "topic": "Transaction Processing",
    "subtopic": "ACID Properties & Crash Recovery",
    "difficulty": "Easy",
    "source": "GATE CSE 2024 Set 2 | Question: 19 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 14)",
    "source_file": "PYQs/CS_extracted/CS/2024_CS2.pdf",
    "source_page": 14,
    "source_qnum": "Q.19",
    "evidence_snippet": "Q.19 Once the DBMS informs the user that a transaction has been successfully completed, its effect should persist even if the system crashes before all its changes are reflected on disk. This property is called (A) durability (B) atomicity (C) consistency (D) isolation",
    "prompt": "Once the DBMS informs the user that a transaction has been successfully completed, its effects must persist even if the system crashes before all changes are reflected on disk. This property is called:",
    "options": [
      "A. Durability",
      "B. Atomicity",
      "C. Consistency",
      "D. Isolation"
    ],
    "correct_option": "A",
    "explanation": "Durability guarantees that once a transaction has committed, its updates survive any subsequent system crash, power failure, or operating system reboot. This is typically implemented via write-ahead logging (WAL) and non-volatile storage flushing.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR database confirms that a doctor's emergency prescription order has been committed. If the hospital database server abruptly loses power, which ACID property ensures the prescription remains in the database?",
        "options": [
          "A. Consistency",
          "B. Atomicity",
          "C. Durability",
          "D. Isolation"
        ],
        "correct_option": "C",
        "explanation": "Durability guarantees persistent retention of committed records across hardware and power failures."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A bank customer receives confirmation that a wire transfer of $10,000 has committed. Seconds later, a power outage crashes the database server. Which ACID property guarantees that the transfer is not lost?",
        "options": [
          "A. Atomicity",
          "B. Durability",
          "C. Isolation",
          "D. Consistency"
        ],
        "correct_option": "B",
        "explanation": "Durability guarantees that committed transaction changes survive crashes and power failures."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "During a Black Friday flash sale, once a customer's payment transaction completes and receives a successful commit confirmation, the updates to inventory and ledger must survive any subsequent server crash or power failure. Which ACID property guarantees this?",
        "options": [
          "A. Durability",
          "B. Atomicity",
          "C. Isolation",
          "D. Consistency"
        ],
        "correct_option": "A",
        "explanation": "Durability guarantees that once a transaction has committed, its updates persist permanently in non-volatile storage, even in the event of system crashes or power outages."
      }
    ]
  },
  {
    "id": "MCQ-022",
    "title": "ER Modeling: Weak Entity Total Participation Invariant",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "ER Modeling & Weak Entities",
    "difficulty": "Easy",
    "source": "GATE CSE 2024 Set 2 | Question: 20 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 14)",
    "source_file": "PYQs/CS_extracted/CS/2024_CS2.pdf",
    "source_page": 14,
    "source_qnum": "Q.20",
    "evidence_snippet": "Q.20 In the context of owner and weak entity sets in the ER (Entity-Relationship) data model, which one of the following statements is TRUE? (A) The weak entity set MUST have total participation in the identifying relationship",
    "prompt": "In the context of owner (identifying) and weak entity sets in the ER (Entity-Relationship) model, which one of the following statements is TRUE?",
    "options": [
      "A. The weak entity set MUST have total participation in the identifying relationship",
      "B. The owner entity set MUST have total participation in the identifying relationship",
      "C. Both weak and owner entity sets MUST have total participation in the identifying relationship",
      "D. Neither weak nor owner entity set is required to have total participation"
    ],
    "correct_option": "A",
    "explanation": "A weak entity cannot exist in the database without being associated with an owner (identifying) entity. Therefore, every weak entity instance must participate in the identifying relationship, meaning the weak entity set MUST have total participation. In contrast, an owner entity instance may exist without having any associated weak entities (partial participation).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a maternity hospital database, Patient is the owner entity and Newborn_Infant is a weak entity. Which participation rule is enforced?",
        "options": [
          "A. Patient must have total participation with Newborn_Infant",
          "B. Both entities must have total participation",
          "C. Newborn_Infant MUST have total participation in the identifying relationship with Patient",
          "D. Newborn_Infant has partial participation"
        ],
        "correct_option": "C",
        "explanation": "A newborn infant cannot exist in the database without an associated mother/patient, requiring total participation."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a corporate banking database, Corporate_Account is the owner entity and Account_Signatory is a weak entity. What participation constraint is mandatory in the ER model?",
        "options": [
          "A. Corporate_Account MUST have total participation in the identifying relationship",
          "B. Account_Signatory MUST have total participation in the identifying relationship",
          "C. Both entities must have partial participation",
          "D. Account_Signatory can have partial participation"
        ],
        "correct_option": "B",
        "explanation": "Weak entities cannot exist without their parent, requiring total participation in the identifying relationship."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce database, OrderItem is a weak entity whose existence depends on the strong entity Order. In the Entity-Relationship (ER) model, what constraint must OrderItem satisfy in the identifying relationship?",
        "options": [
          "A. Total participation (double line) in the identifying relationship",
          "B. Partial participation with no primary key",
          "C. Disjoint cardinality constraint with zero attributes",
          "D. Total participation of Order in OrderItem"
        ],
        "correct_option": "A",
        "explanation": "A weak entity cannot exist without its identifying strong entity, and therefore must have total participation in the identifying relationship."
      }
    ]
  },
  {
    "id": "MCQ-023",
    "title": "Two-Phase Locking (2PL) Protocol Phase Transition Invariant",
    "topic": "Concurrency Control",
    "subtopic": "Two-Phase Locking (2PL)",
    "difficulty": "Medium",
    "source": "GATE CSE 2024 Set 2 | Question: 27 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 19)",
    "source_file": "PYQs/CS_extracted/CS/2024_CS2.pdf",
    "source_page": 19,
    "source_qnum": "Q.27",
    "evidence_snippet": "Q.27 Which of the following statements about the Two Phase Locking (2PL) protocol is/are TRUE? (A) 2PL permits only serializable schedules (C) With 2PL, once a lock is released on any data item inside a transaction, no more locks on any data item can be obtained inside that transaction",
    "prompt": "Which fundamental invariant defines the Two-Phase Locking (2PL) protocol?",
    "options": [
      "A. Once a lock is released on any data item by a transaction, no new locks can be acquired by that transaction",
      "B. All locks must be released before any data item can be updated",
      "C. Shared locks cannot be converted to exclusive locks under any circumstances",
      "D. A transaction releases all its locks at the exact moment it starts execution"
    ],
    "correct_option": "A",
    "explanation": "The defining rule of 2PL is the division of transaction execution into two distinct phases: 1) Growing Phase: locks may be acquired but none released; 2) Shrinking Phase: locks may be released, but no new locks may be acquired. Once a single lock is released, the transaction enters the shrinking phase and can never obtain another lock.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital medication dispenser transaction holds locks on drug inventory records under 2PL. Once it releases the lock on Morphine_Vials, what is legally disallowed?",
        "options": [
          "A. Writing log records to the audit trail",
          "B. Releasing the lock on Saline_Bags",
          "C. Acquiring a lock on Syringe_Stock or any other inventory item",
          "D. Issuing a COMMIT statement"
        ],
        "correct_option": "C",
        "explanation": "In 2PL, no new lock acquisitions are permitted after the first lock release."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated securities settlement engine executing under Two-Phase Locking (2PL), what behavior is strictly prohibited once the settlement transaction releases an exclusive lock on an asset ledger?",
        "options": [
          "A. Committing the transaction to disk",
          "B. Acquiring any subsequent shared or exclusive lock on any data item",
          "C. Reading values of already locked memory items",
          "D. Releasing other locks currently held by the transaction"
        ],
        "correct_option": "B",
        "explanation": "Under 2PL, releasing any lock transitions the transaction into the shrinking phase, forbidding further lock acquisitions."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce inventory management system using Two-Phase Locking (2PL), what action marks the transition of a checkout transaction from the Growing phase to the Shrinking phase?",
        "options": [
          "A. Releasing the first lock currently held by the transaction",
          "B. Acquiring an exclusive lock on the warehouse table",
          "C. Reading an uncommitted inventory tuple",
          "D. Starting the transaction"
        ],
        "correct_option": "A",
        "explanation": "Under 2PL, a transaction cannot acquire any locks once it releases a lock. The instant a transaction releases its first lock, the growing phase ends and the shrinking phase begins."
      }
    ]
  },
  {
    "id": "MCQ-024",
    "title": "Relational Algebra Cross Products for At-Least-K Cardinality",
    "topic": "Relational Algebra",
    "subtopic": "Cross Product Count for Minimum Cardinality",
    "difficulty": "Medium",
    "source": "GATE CSE 2024 Set 2 | Question: 45 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 31)",
    "source_file": "PYQs/CS_extracted/CS/2024_CS2.pdf",
    "source_page": 31,
    "source_qnum": "Q.45",
    "evidence_snippet": "Q.45 The relation schema, Person(pid,city), describes the city of residence for every person uniquely identified by pid. The following relational algebra operators are available: selection, projection, cross product, and rename. To find the list of cities where at least 3 persons reside, using the above operators, the minimum number of cross product operations that must be used is (A) 1 (B) 2 (C) 3 (D) 4",
    "prompt": "Consider the relation Person(pid, city), where pid is a unique identifier. Using only selection, projection, cross product, and rename, what is the minimum number of cross product operations required to find all cities where at least 3 distinct persons reside?",
    "options": [
      "A. 2",
      "B. 1",
      "C. 3",
      "D. 4"
    ],
    "correct_option": "A",
    "explanation": "To find cities with at least 3 distinct persons, we need to compare three distinct person tuples from the same city: (P1.city = P2.city AND P2.city = P3.city AND P1.pid != P2.pid AND P1.pid != P3.pid AND P2.pid != P3.pid). Combining three instances of the Person relation requires 2 cross product operations: (Person P1 × Person P2) × Person P3.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an epidemiological registry Infection_Cases(case_id, district), what is the minimum number of cross products required to find districts reporting at least 3 distinct cases using basic relational algebra?",
        "options": [
          "A. 3 cross products",
          "B. 1 cross product",
          "C. 2 cross products",
          "D. 0 cross products"
        ],
        "correct_option": "C",
        "explanation": "To select 3 distinct tuples (C1, C2, C3) belonging to the same district, 2 cross products are required: (C1 × C2) × C3."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an investment bank portfolio table Holdings(holding_id, branch_id), what is the minimum number of Cartesian product operations needed to identify branches holding at least 3 distinct assets without using GROUP BY?",
        "options": [
          "A. 1 Cartesian product",
          "B. 2 Cartesian products",
          "C. 3 Cartesian products",
          "D. 4 Cartesian products"
        ],
        "correct_option": "B",
        "explanation": "Comparing 3 distinct holding instances requires joining 3 copies of the table, which requires 2 cross product operations."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce analytics query needs to find customers who have purchased at least 3 distinct products in a single order using basic relational algebra (select, project, cross-product). What is the minimum number of Cartesian cross products of Order_Items with itself required to compare 3 distinct product IDs for the same order?",
        "options": [
          "A. 2 cross products (joining 3 instances of Order_Items: I1 × I2 × I3)",
          "B. 1 cross product",
          "C. 3 cross products",
          "D. 4 cross products"
        ],
        "correct_option": "A",
        "explanation": "To reference 3 distinct item tuples (I1, I2, I3) of the same order simultaneously in a selection condition, 3 instances of the relation must be combined, requiring 2 cross products: (I1 × I2) × I3."
      }
    ]
  },
  {
    "id": "MCQ-025",
    "title": "Relational Algebra Set Difference for Referential Inclusion",
    "topic": "Relational Algebra",
    "subtopic": "Set Difference for Universal Containment",
    "difficulty": "Medium",
    "source": "GATE DA 2024 | Question: 26 (PYQs/DA_extracted/DA/DA2024.pdf, Page 16)",
    "source_file": "PYQs/DA_extracted/DA/DA2024.pdf",
    "source_page": 16,
    "source_qnum": "Q.26",
    "evidence_snippet": "Q.26 Consider a database that includes the following relations: Defender(name, rating, side, goals), Forward(name, rating, assists, goals), Team(name, club, price). Which ONE of the following relational algebra expressions checks that every name occurring in Team appears in either Defender or Forward, where 𝜙 denotes the empty set? (C) Π𝑛𝑎𝑚𝑒(Team) ∖(Π𝑛𝑎𝑚𝑒(Defender)∪Π𝑛𝑎𝑚𝑒(Forward)) = 𝜙",
    "prompt": "Consider relations Defender(name, ...), Forward(name, ...), and Team(name, ...). Which relational algebra expression checks that every name occurring in Team appears in either Defender or Forward (where ∅ denotes the empty set)?",
    "options": [
      "A. ∏_name(Team) ∖ ( ∏_name(Defender) ∪ ∏_name(Forward) ) = ∅",
      "B. ∏_name(Team) ∖ ( ∏_name(Defender) ∩ ∏_name(Forward) ) = ∅",
      "C. ( ∏_name(Defender) ∪ ∏_name(Forward) ) ∖ ∏_name(Team) = ∅",
      "D. ( ∏_name(Defender) ∩ ∏_name(Forward) ) ∖ ∏_name(Team) = ∅"
    ],
    "correct_option": "A",
    "explanation": "To verify that every name in Team appears in either Defender or Forward (i.e., ∏_name(Team) ⊆ ∏_name(Defender) ∪ ∏_name(Forward)), we subtract the union from Team. If no names remain in Team that are outside the union, the set difference equals the empty set ∅.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital emergency intake: Inpatients(patient_id), Trauma_Cases(patient_id), Medical_Cases(patient_id). Which relational algebra expression asserts that all inpatients belong to either trauma or medical admissions?",
        "options": [
          "A. ∏_patient_id(Inpatients) ∖ ( ∏_patient_id(Trauma_Cases) ∩ ∏_patient_id(Medical_Cases) ) = ∅",
          "B. ( ∏_patient_id(Trauma_Cases) ∪ ∏_patient_id(Medical_Cases) ) ∖ ∏_patient_id(Inpatients) = ∅",
          "C. ∏_patient_id(Inpatients) ∖ ( ∏_patient_id(Trauma_Cases) ∪ ∏_patient_id(Medical_Cases) ) = ∅",
          "D. ∏_patient_id(Trauma_Cases) ∪ ∏_patient_id(Medical_Cases) = ∅"
        ],
        "correct_option": "C",
        "explanation": "A ∖ (B ∪ C) = ∅ checks that every element of A is contained in B or C."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial compliance audit: Account_Holders(id), Retail_Clients(id), Corporate_Clients(id). Which expression asserts that every account holder is classified as either a retail or corporate client?",
        "options": [
          "A. ( ∏_id(Retail_Clients) ∪ ∏_id(Corporate_Clients) ) ∖ ∏_id(Account_Holders) = ∅",
          "B. ∏_id(Account_Holders) ∖ ( ∏_id(Retail_Clients) ∪ ∏_id(Corporate_Clients) ) = ∅",
          "C. ∏_id(Account_Holders) ∖ ( ∏_id(Retail_Clients) ∩ ∏_id(Corporate_Clients) ) = ∅",
          "D. ∏_id(Retail_Clients) ∩ ∏_id(Corporate_Clients) = ∅"
        ],
        "correct_option": "B",
        "explanation": "Subtracting the union of valid client categories from Account_Holders tests whether all holders belong to at least one category."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce platform, Registered_Users(UserID) lists all registered users and Active_Shoppers(UserID) lists users who placed an order this month. Which relational algebra expression finds users who have NEVER placed an order this month?",
        "options": [
          "A. Registered_Users − Active_Shoppers",
          "B. Active_Shoppers − Registered_Users",
          "C. Registered_Users ∩ Active_Shoppers",
          "D. Registered_Users ⨝ Active_Shoppers"
        ],
        "correct_option": "A",
        "explanation": "The set difference R − S returns tuples present in R that do not appear in S, which gives registered users who have not placed an order."
      }
    ]
  },
  {
    "id": "MCQ-026",
    "title": "Functional Dependency Derivation from Attribute Closure",
    "topic": "Functional Dependencies",
    "subtopic": "Attribute Closure and Derivability",
    "difficulty": "Medium",
    "source": "GATE DA 2024 | Question: 46 (PYQs/DA_extracted/DA/DA2024.pdf, Page 29)",
    "source_file": "PYQs/DA_extracted/DA/DA2024.pdf",
    "source_page": 29,
    "source_qnum": "Q.46",
    "evidence_snippet": "Q.46 Given the relational schema 𝑅= (𝑈,𝑉, 𝑊, 𝑋, 𝑌, 𝑍) and the set of functional dependencies: {𝑈→𝑉, 𝑈→𝑊, 𝑊𝑋→𝑌, 𝑊𝑋→𝑍, 𝑉→𝑋}. Which of the following functional dependencies can be derived from the above set? (A) 𝑉𝑊→𝑌𝑍",
    "prompt": "Given relational schema R = (U, V, W, X, Y, Z) and functional dependencies F = {U -> V, U -> W, WX -> Y, WX -> Z, V -> X}. Which of the following functional dependencies can be derived from F?",
    "options": [
      "A. VW -> YZ",
      "B. VW -> U",
      "C. X -> YZ",
      "D. W -> Y"
    ],
    "correct_option": "A",
    "explanation": "To test if VW -> YZ can be derived, compute the attribute closure (VW)+ with respect to F:\n1. (VW)+ = {V, W}\n2. Using V -> X: (VW)+ = {V, W, X}\n3. Using WX -> Y and WX -> Z: (VW)+ = {V, W, X, Y, Z}\nSince {Y, Z} ⊆ (VW)+, the dependency VW -> YZ holds.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an electronic patient record with attributes (U, V, W, X, Y, Z) and dependencies {U->V, U->W, WX->Y, WX->Z, V->X}, which functional dependency is valid?",
        "options": [
          "A. W -> Z",
          "B. VW -> U",
          "C. VW -> YZ",
          "D. X -> Y"
        ],
        "correct_option": "C",
        "explanation": "Closing {V, W} under F yields {V, W, X, Y, Z}, thereby proving VW -> YZ."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial asset ledger with attributes (U, V, W, X, Y, Z) and dependencies {U->V, U->W, WX->Y, WX->Z, V->X}, which dependency holds?",
        "options": [
          "A. VW -> U",
          "B. VW -> YZ",
          "C. X -> YZ",
          "D. W -> Y"
        ],
        "correct_option": "B",
        "explanation": "(VW)+ contains X via V->X, which unlocks WX->Y and WX->Z, deriving VW -> YZ."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce catalog relation Product_SKU(P, S, C, M) with FDs P -> S and S -> C, which of the following functional dependencies is logically implied?",
        "options": [
          "A. P -> C",
          "B. S -> P",
          "C. C -> M",
          "D. M -> P"
        ],
        "correct_option": "A",
        "explanation": "By the Transitivity Axiom of functional dependencies, if P -> S and S -> C, then P -> C."
      }
    ]
  },
  {
    "id": "MCQ-027",
    "title": "Cascading Rollback on Abort Due to Dirty Reads",
    "topic": "Concurrency Control",
    "subtopic": "Cascading Rollback & Dirty Reads",
    "difficulty": "Medium",
    "source": "GATE CSE 2025 Set 1 | Question: 15 (PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf, Page 15)",
    "source_file": "PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf",
    "source_page": 15,
    "source_qnum": "Q.15",
    "evidence_snippet": "Q.15 A schedule of three database transactions 𝑇1, 𝑇2, and 𝑇3 is shown. 𝑅𝑖(𝐴) and 𝑊𝑖(𝐴) denote read and write of data item 𝐴 by transaction 𝑇𝑖, 𝑖= 1,2,3. The transaction 𝑇1 aborts at the end. Which other transaction(s) will be required to be rolled back? 𝑅1(𝑋) 𝑊1(𝑌) 𝑅2(𝑋) 𝑅2(𝑌) 𝑅3(𝑌) 𝐴𝐵𝑂𝑅𝑇(𝑇1)",
    "prompt": "Consider schedule S of three transactions: R1(X) W1(Y) R2(X) R2(Y) R3(Y) ABORT(T1). If transaction T1 aborts, which other transaction(s) must undergo cascading rollback?",
    "options": [
      "A. Both T2 and T3",
      "B. Only T2",
      "C. Only T3",
      "D. Neither T2 nor T3"
    ],
    "correct_option": "A",
    "explanation": "Transaction T1 writes data item Y with W1(Y). Subsequently, transaction T2 reads Y (R2(Y)) and transaction T3 reads Y (R3(Y)) before T1 commits. Because both T2 and T3 performed dirty reads on data item Y produced by T1, aborting T1 forces both T2 and T3 to be rolled back to maintain consistency.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an intensive care medication system, physician transaction T1 writes a dosage Y and aborts. Meanwhile, nurse transaction T2 and pharmacy transaction T3 read Y. Which transactions must be aborted?",
        "options": [
          "A. Only T3",
          "B. Only T2",
          "C. Both T2 and T3",
          "D. Neither T2 nor T3"
        ],
        "correct_option": "C",
        "explanation": "Reading uncommitted dirty writes causes cascading aborts for all downstream consumers (T2 and T3)."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an interbank settlement engine, transaction T1 writes to account balance Y and subsequently aborts. Prior to T1's abort, transaction T2 and T3 read the uncommitted balance Y. Which transactions must be rolled back?",
        "options": [
          "A. Only T2",
          "B. Both T2 and T3",
          "C. Only T3",
          "D. Neither transaction"
        ],
        "correct_option": "B",
        "explanation": "Both T2 and T3 read uncommitted dirty data written by T1, mandating cascading rollback for both."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "During checkout, Transaction T1 writes uncommitted stock to SKU_101. Transaction T2 reads this uncommitted stock and computes total price. If T1 subsequently aborts and rolls back, what must happen to T2 to maintain consistency?",
        "options": [
          "A. Cascading rollback: T2 must also be aborted and rolled back because it performed a dirty read of uncommitted data",
          "B. T2 is allowed to commit with the stale data",
          "C. The database converts T2 into a background daemon",
          "D. T1 is forced to re-execute without aborting"
        ],
        "correct_option": "A",
        "explanation": "Reading uncommitted data written by a transaction that subsequently aborts creates a dirty read anomaly, requiring cascading rollback of the dependent transaction to maintain consistency."
      }
    ]
  },
  {
    "id": "MCQ-028",
    "title": "Relational Schema Arity (Degree) Definition",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "Schema Arity vs Relation Cardinality",
    "difficulty": "Easy",
    "source": "GATE CSE 2023 | Question: 16 (PYQs/CS_extracted/CS/2023_CS.pdf, Page 13)",
    "source_file": "PYQs/CS_extracted/CS/2023_CS.pdf",
    "source_page": 13,
    "source_qnum": "Q.16",
    "evidence_snippet": "Q.16 Which one of the options given below refers to the degree (or arity) of a relation in relational database systems? (A) Number of attributes of its relation schema. (B) Number of tuples stored in the relation.",
    "prompt": "Which of the following refers to the degree (or arity) of a relation in relational database systems?",
    "options": [
      "A. Number of attributes of its relation schema",
      "B. Number of tuples stored in the relation instance",
      "C. Total number of data entries across all cells",
      "D. Number of candidate keys defined on the relation"
    ],
    "correct_option": "A",
    "explanation": "In relational database terminology:\n- Degree (or Arity) is the total number of attributes (columns) in the relation schema.\n- Cardinality is the total number of tuples (rows) currently present in the relation instance.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR table Vitals_Log(log_id, patient_id, heart_rate, bp, o2_sat, timestamp) has 6 columns. What database term describes this count?",
        "options": [
          "A. The cardinality of the vitals dataset",
          "B. The normal form level of the log",
          "C. The degree (arity) of the relation schema",
          "D. The transaction isolation level"
        ],
        "correct_option": "C",
        "explanation": "Degree (or arity) is defined as the number of attributes comprising the schema."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When designing a financial risk relation schema Risk_Metrics(id, exposure, var, cvar, rating), what metric does the integer 5 represent?",
        "options": [
          "A. The cardinality of the relation instance",
          "B. The degree (or arity) of the relation schema",
          "C. The index depth of the table",
          "D. The number of candidate keys"
        ],
        "correct_option": "B",
        "explanation": "The number of attributes in a relational schema is defined as its degree or arity."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce product table Product(SKU, Title, Brand, Category, Price, StockQuantity) currently stores 100,000 product rows. What is the arity (degree) of this relation?",
        "options": [
          "A. 6 (the number of attributes/columns)",
          "B. 100,000 (the number of tuples/rows)",
          "C. 600,000 (the total number of cells)",
          "D. 1 (the number of primary keys)"
        ],
        "correct_option": "A",
        "explanation": "In the formal relational model, the arity (or degree) of a relation is defined as the number of attributes (columns) in its schema, which is 6."
      }
    ]
  },
  {
    "id": "MCQ-029",
    "title": "Relational Division Formal Algebraic Expression",
    "topic": "Relational Algebra",
    "subtopic": "Relational Division Implementation",
    "difficulty": "Hard",
    "source": "GATE CSE 2022 | Question: 25 (PYQs/CS_extracted/CS/2022_CS.pdf, Page 20)",
    "source_file": "PYQs/CS_extracted/CS/2022_CS.pdf",
    "source_page": 20,
    "source_qnum": "Q.25",
    "evidence_snippet": "Q.25 Consider the following three relations in a relational database. Employee(eId, Name), Brand(bId, bName), Own(eId, bId). Which of the following relational algebra expressions return the set of eIds who own all the brands?",
    "prompt": "Consider relations Employee(eId, Name), Brand(bId, bName), and Own(eId, bId). Which relational algebra expression correctly returns the set of eIds of employees who own ALL the brands?",
    "options": [
      "A. ∏_eId (Own) − ∏_eId ( ( ∏_eId (Own) × ∏_bId (Brand) ) − Own )",
      "B. ∏_eId (Own) − ∏_eId ( ∏_eId (Own) × ∏_bId (Brand) )",
      "C. ∏_eId (Own) ∪ ∏_eId ( ( ∏_eId (Own) × ∏_bId (Brand) ) − Own )",
      "D. ∏_eId ( ∏_eId (Own) × ∏_bId (Brand) )"
    ],
    "correct_option": "A",
    "explanation": "This is the standard algebraic formulation of relational division Own ÷ Brand:\n1. ∏_eId(Own) × ∏_bId(Brand) forms all possible combinations of employees and brands.\n2. Subtracting Own gives all combinations of (employee, brand) that the employee DOES NOT own.\n3. Projecting eId yields all employees who fail to own at least one brand.\n4. Subtracting those disqualified employees from all employees (∏_eId(Own)) leaves precisely those employees who own all brands.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital credentialing registry: Surgeon(doc_id), Procedure(proc_id), Certified(doc_id, proc_id). Which relational algebra expression identifies surgeons certified in ALL procedures?",
        "options": [
          "A. ∏_doc_id(Certified) ∪ ∏_doc_id(Procedure)",
          "B. ∏_doc_id(Certified) − ∏_doc_id(Certified × Procedure)",
          "C. ∏_doc_id(Certified) − ∏_doc_id( ( ∏_doc_id(Certified) × ∏_proc_id(Procedure) ) − Certified )",
          "D. ∏_doc_id(Procedure) − ∏_doc_id(Certified)"
        ],
        "correct_option": "C",
        "explanation": "Standard relational division formula finds doctors with no uncertified procedures."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an institutional securities desk: Trader(trader_id), Product(prod_id), Sells(trader_id, prod_id). Which expression finds traders who trade every available product?",
        "options": [
          "A. ∏_trader_id(Sells) ∩ ∏_trader_id(Product)",
          "B. ∏_trader_id(Sells) − ∏_trader_id( ( ∏_trader_id(Sells) × ∏_prod_id(Product) ) − Sells )",
          "C. ∏_trader_id(Sells) − ∏_prod_id(Product)",
          "D. ∏_trader_id( ( ∏_trader_id(Sells) × ∏_prod_id(Product) ) )"
        ],
        "correct_option": "B",
        "explanation": "Relational division implemented via double negation: all traders minus those with at least one missing product."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Let Purchased(CustomerID, VendorID) and All_Vendors(VendorID) be e-commerce relations. Which formula expresses the relational division Purchased ÷ All_Vendors using basic relational algebra?",
        "options": [
          "A. ∏_CustomerID(Purchased) − ∏_CustomerID( (∏_CustomerID(Purchased) × All_Vendors) − Purchased )",
          "B. ∏_CustomerID(Purchased) ∩ ∏_VendorID(All_Vendors)",
          "C. Purchased × All_Vendors",
          "D. ∏_CustomerID(Purchased ⨝ All_Vendors)"
        ],
        "correct_option": "A",
        "explanation": "The formal algebraic expansion of relational division R(X, Y) ÷ S(Y) is ∏_X(R) − ∏_X( (∏_X(R) × S) − R )."
      }
    ]
  },
  {
    "id": "MCQ-030",
    "title": "Identification of 3NF Schemas Violating BCNF",
    "topic": "Normalization & Functional Dependencies",
    "subtopic": "3NF vs BCNF Distinction",
    "difficulty": "Medium",
    "source": "GATE CSE 2018 | Question: 42 (PYQs/CS_extracted/CS/2018_CS.pdf, Page 18)",
    "source_file": "PYQs/CS_extracted/CS/2018_CS.pdf",
    "source_page": 18,
    "source_qnum": "Q.42",
    "evidence_snippet": "Q.42 Consider the following four relational schemas. Schema I: Registration (rollno, courses) rollno  courses. Schema II: Registration (rollno, courseid, email) rollno, courseid  email, email  rollno. Which one of the relational schemas above is in 3NF but not in BCNF? (B) Schema II",
    "prompt": "Consider relation Schema II: Registration(rollno, courseid, email) with functional dependencies: { (rollno, courseid) -> email, email -> rollno }. What is the highest normal form satisfied by this schema?",
    "options": [
      "A. 3NF (satisfies 3NF but violates BCNF)",
      "B. BCNF",
      "C. 2NF only",
      "D. 1NF only"
    ],
    "correct_option": "A",
    "explanation": "For Schema II:\n- Candidate keys are (rollno, courseid) and (email, courseid).\n- Prime attributes are {rollno, courseid, email}.\n- Dependency (rollno, courseid) -> email has a superkey on the LHS.\n- Dependency email -> rollno has LHS 'email' which is NOT a superkey (violating BCNF). However, the RHS 'rollno' is a prime attribute, which is permitted in 3NF.\nTherefore, the schema is in 3NF, but NOT in BCNF.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital bed registry Bed_Allocation(bed_no, ward_id, nfc_tag) has FDs: { (bed_no, ward_id) -> nfc_tag, nfc_tag -> bed_no }. In which normal form does this table reside?",
        "options": [
          "A. BCNF",
          "B. 2NF only",
          "C. 3NF but not BCNF",
          "D. 4NF"
        ],
        "correct_option": "C",
        "explanation": "All attributes are prime, satisfying 3NF, but nfc_tag is not a superkey, failing BCNF."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A fintech clearing table Accounts(tax_id, acc_num, swift_code) has FDs: { (tax_id, acc_num) -> swift_code, swift_code -> tax_id }. What is the highest normal form satisfied?",
        "options": [
          "A. BCNF",
          "B. 3NF but not BCNF",
          "C. 2NF only",
          "D. 1NF only"
        ],
        "correct_option": "B",
        "explanation": "swift_code -> tax_id has a prime RHS (tax_id), satisfying 3NF, but swift_code is not a superkey, violating BCNF."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce warehouse relation Storage(Warehouse, Bay, Manager) has candidate keys {Warehouse, Bay} and {Warehouse, Manager} with functional dependency Manager -> Bay. Why is this relation in 3NF but NOT in BCNF?",
        "options": [
          "A. In FD Manager -> Bay, Manager is not a superkey, but Bay is a prime attribute (part of candidate key {Warehouse, Bay})",
          "B. The relation has multi-valued dependencies",
          "C. The relation has no candidate keys",
          "D. Manager is a primary key"
        ],
        "correct_option": "A",
        "explanation": "In 3NF, for every FD X -> A, either X is a superkey OR A is a prime attribute. Here Bay is prime, so 3NF holds. But Manager is not a superkey, so BCNF is violated."
      }
    ]
  },
  {
    "id": "MCQ-031",
    "title": "Superkey Identification from Primary Key Invariant",
    "topic": "Functional Dependencies",
    "subtopic": "Superkeys vs Candidate Keys",
    "difficulty": "Easy",
    "source": "GATE CSE 2016 Set 1 | Question: 21 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 10)",
    "source_file": "PYQs/CS_extracted/CS/2016_CS.pdf",
    "source_page": 10,
    "source_qnum": "Q.21",
    "evidence_snippet": "Q.21 Which of the following is NOT a superkey in a relational schema with attributes V, W, X, Y, Z and primary key V Y? (A) VXYZ (B) VWXZ (C) VWXY (D) VWXYZ",
    "prompt": "Which of the following is NOT a superkey in a relational schema with attributes V, W, X, Y, Z and primary key VY?",
    "options": [
      "A. VWXZ",
      "B. VXYZ",
      "C. VWXY",
      "D. VWXYZ"
    ],
    "correct_option": "A",
    "explanation": "A superkey is any set of attributes that contains a candidate key (or primary key) as a subset. Since VY is the primary key, any valid superkey MUST contain both V and Y.\n- VXYZ contains {V, Y} (Superkey)\n- VWXZ contains {V} but lacks {Y} (NOT a superkey)\n- VWXY contains {V, Y} (Superkey)\n- VWXYZ contains {V, Y} (Superkey)",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR patient diagnostic schema has attributes V, W, X, Y, Z and primary key VY. Which attribute set is NOT a superkey?",
        "options": [
          "A. VWXY",
          "B. VXYZ",
          "C. VWXZ",
          "D. VWXYZ"
        ],
        "correct_option": "C",
        "explanation": "Attribute Y is absent from VWXZ, so it cannot uniquely identify tuples and is not a superkey."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated forex trading relation with attributes V, W, X, Y, Z and primary key VY, which attribute combination fails to be a superkey?",
        "options": [
          "A. VXYZ",
          "B. VWXZ",
          "C. VWXY",
          "D. VWXYZ"
        ],
        "correct_option": "B",
        "explanation": "VWXZ fails to include attribute Y, which is mandatory for any superkey containing primary key VY."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce user table Shopper(ShopperID, Email, Phone, Address) where ShopperID is designated as the primary key, which of the following combinations is GUARANTEED to be a superkey?",
        "options": [
          "A. {ShopperID, Email, Phone}",
          "B. {Email, Phone}",
          "C. {Address}",
          "D. {Email}"
        ],
        "correct_option": "A",
        "explanation": "Any superset of a candidate/primary key is by definition a superkey. Since ShopperID is the primary key, adding any other attributes ({ShopperID, Email, Phone}) forms a valid superkey."
      }
    ]
  },
  {
    "id": "MCQ-032",
    "title": "ACID Properties: Exclusion of Operational Properties",
    "topic": "Transaction Processing",
    "subtopic": "ACID Properties of Transactions",
    "difficulty": "Easy",
    "source": "GATE CSE 2016 Set 1 | Question: 22 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 10)",
    "source_file": "PYQs/CS_extracted/CS/2016_CS.pdf",
    "source_page": 10,
    "source_qnum": "Q.22",
    "evidence_snippet": "Q.22 Which one of the following is NOT a part of the ACID properties of database transactions? (A) Atomicity (B) Consistency (C) Isolation (D) Deadlock-freedom",
    "prompt": "Which one of the following is NOT a part of the ACID properties of database transactions?",
    "options": [
      "A. Deadlock-freedom",
      "B. Atomicity",
      "C. Consistency",
      "D. Isolation"
    ],
    "correct_option": "A",
    "explanation": "ACID stands for:\n- A: Atomicity (all or nothing execution)\n- C: Consistency (preserves database integrity constraints)\n- I: Isolation (concurrent transactions execute without interference)\n- D: Durability (committed changes persist across system failures)\nDeadlock-freedom is an operational concurrency/scheduling property, NOT an ACID property.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital health record database enforces ACID transaction guarantees. Which of the following is NOT an ACID requirement?",
        "options": [
          "A. Durability",
          "B. Consistency",
          "C. Deadlock-freedom",
          "D. Atomicity"
        ],
        "correct_option": "C",
        "explanation": "Deadlock-freedom is a concurrency scheduling technique, not an ACID guarantee."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When evaluating a core banking transaction manager, which property is NOT an acronym element of ACID?",
        "options": [
          "A. Atomicity",
          "B. Deadlock-freedom",
          "C. Consistency",
          "D. Isolation"
        ],
        "correct_option": "B",
        "explanation": "ACID stands for Atomicity, Consistency, Isolation, and Durability; deadlock-freedom is not one of them."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In database transaction management for e-commerce checkouts, which of the following is NOT one of the formal ACID properties?",
        "options": [
          "A. Availability",
          "B. Atomicity",
          "C. Consistency",
          "D. Durability"
        ],
        "correct_option": "A",
        "explanation": "ACID stands for Atomicity, Consistency, Isolation, and Durability. Availability is part of the CAP theorem, not ACID."
      }
    ]
  },
  {
    "id": "MCQ-033",
    "title": "Second Normal Form (2NF) Partial Dependency Elimination",
    "topic": "Normalization & Functional Dependencies",
    "subtopic": "Second Normal Form (2NF)",
    "difficulty": "Medium",
    "source": "GATE CSE 2016 Set 1 | Question: 23 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 11)",
    "source_file": "PYQs/CS_extracted/CS/2016_CS.pdf",
    "source_page": 11,
    "source_qnum": "Q.23",
    "evidence_snippet": "Q.23 A database of research articles in a journal uses the following schema. (VOLUME, NUMBER, STARTPAGE, ENDPAGE, TITLE, YEAR, PRICE). The primary key is (VOLUME, NUMBER, STARTPAGE, ENDPAGE) and (VOLUME, NUMBER) -> YEAR. Which is the weakest normal form that the new database satisfies, but the old one does not? (B) 2NF",
    "prompt": "A relation R(VOLUME, NUMBER, STARTPAGE, ENDPAGE, TITLE, YEAR, PRICE) has primary key (VOLUME, NUMBER, STARTPAGE, ENDPAGE) and dependency (VOLUME, NUMBER) -> YEAR. When decomposed into R1(VOLUME, NUMBER, STARTPAGE, ENDPAGE, TITLE, PRICE) and R2(VOLUME, NUMBER, YEAR), what is the weakest normal form satisfied by the new database that the old one violated?",
    "options": [
      "A. 2NF",
      "B. 1NF",
      "C. 3NF",
      "D. BCNF"
    ],
    "correct_option": "A",
    "explanation": "In the original schema, the non-prime attribute YEAR depended on a proper subset (VOLUME, NUMBER) of the candidate key (VOLUME, NUMBER, STARTPAGE, ENDPAGE), representing a partial functional dependency. This violated 2NF. Decomposing the relation into R1 and R2 eliminates this partial dependency, making the new database satisfy 2NF.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital surgery log Surgery(hospital_id, room_no, surgery_date, surgeon_id, room_type) with key (hospital_id, room_no, surgery_date) has (hospital_id, room_no) -> room_type. Moving room_type to a separate Operating_Room table brings the schema into which normal form?",
        "options": [
          "A. 3NF",
          "B. 1NF",
          "C. 2NF",
          "D. BCNF"
        ],
        "correct_option": "C",
        "explanation": "Eliminating partial key dependencies directly satisfies 2NF."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A syndicated loan contract table Loan(deal_id, tranche_id, facility_id, currency, tranche_rate) has primary key (deal_id, tranche_id, facility_id) and partial dependency (deal_id, tranche_id) -> tranche_rate. Splitting out Tranche(deal_id, tranche_id, tranche_rate) elevates the design to which normal form?",
        "options": [
          "A. 1NF",
          "B. 2NF",
          "C. 3NF",
          "D. BCNF"
        ],
        "correct_option": "B",
        "explanation": "Removing partial dependencies of non-prime attributes on a subset of the candidate key satisfies 2NF."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce order-line relation Order_Item(OrderID, ItemID, Quantity, OrderDate) has composite primary key {OrderID, ItemID}. If functional dependency OrderID -> OrderDate exists, why does it violate Second Normal Form (2NF)?",
        "options": [
          "A. Because non-prime attribute OrderDate is functionally dependent on a proper subset of the composite candidate key (partial dependency)",
          "B. Because OrderDate is a transitive dependency",
          "C. Because 2NF disallows integers",
          "D. Because Order_Item has too many rows"
        ],
        "correct_option": "A",
        "explanation": "2NF requires that the relation is in 1NF and no non-prime attribute is partially dependent on any candidate key. Here OrderDate depends on OrderID alone, which is a proper subset of {OrderID, ItemID}."
      }
    ]
  },
  {
    "id": "MCQ-034",
    "title": "Strict Two-Phase Locking with Resource Ordering Guarantees",
    "topic": "Concurrency Control",
    "subtopic": "Lock Ordering and Deadlock Prevention",
    "difficulty": "Medium",
    "source": "GATE CSE 2016 Set 1 | Question: 51 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 19)",
    "source_file": "PYQs/CS_extracted/CS/2016_CS.pdf",
    "source_page": 19,
    "source_qnum": "Q.51",
    "evidence_snippet": "Q.51 Consider the following two phase locking protocol. Suppose a transaction T accesses a certain set of objects {O1,...,Ok}. Step 1. T acquires exclusive locks to O1, ..., Ok in increasing order of their addresses. Step 2. Operations performed. Step 3. All locks are released. This protocol will (A) guarantee serializability and deadlock-freedom",
    "prompt": "Consider a concurrency protocol where every transaction T: (1) acquires exclusive locks on all required data objects in strictly increasing order of their memory addresses, (2) performs all read/write operations, and (3) releases all locks at termination. What guarantees does this protocol provide?",
    "options": [
      "A. Guarantees both serializability and deadlock-freedom",
      "B. Guarantees serializability but not deadlock-freedom",
      "C. Guarantees deadlock-freedom but not serializability",
      "D. Guarantees neither serializability nor deadlock-freedom"
    ],
    "correct_option": "A",
    "explanation": "1. Serializability: Because transactions acquire all locks before releasing any locks, this is a form of conservative (or strict) 2PL, which guarantees conflict serializability.\n2. Deadlock-freedom: Imposing a total global order on lock acquisition (strictly increasing memory addresses) eliminates circular wait conditions, thereby guaranteeing complete immunity from deadlocks.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An intensive care EMR manages infusion pump updates by acquiring locks in ascending order of Device_ID and releasing all at transaction completion. What does this guarantee?",
        "options": [
          "A. Deadlock freedom but non-serializable schedules",
          "B. Only cascading rollbacks",
          "C. Both conflict serializability and freedom from deadlocks",
          "D. Neither property"
        ],
        "correct_option": "C",
        "explanation": "Strict 2PL ensures conflict serializability, and global resource ordering prevents deadlocks."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a high-frequency trading matching engine, transactions lock trading books strictly by ascending numeric BookID before performing updates, releasing all locks at commit. What properties are guaranteed?",
        "options": [
          "A. Serializability only, deadlocks may occur",
          "B. Both serializability and deadlock-freedom",
          "C. Deadlock-freedom only, dirty reads may occur",
          "D. Neither serializability nor deadlock-freedom"
        ],
        "correct_option": "B",
        "explanation": "2PL guarantees serializability; acquiring locks in global ascending order prevents circular wait deadlocks."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To prevent deadlocks during high-concurrency flash sales while maintaining strict serializability, an e-commerce database engine enforces Strict 2PL and requires transactions to request item locks in global ascending order of SKU ID. What does this guarantee?",
        "options": [
          "A. Both serializability and deadlock-freedom",
          "B. Serializability only, deadlocks may still occur",
          "C. Deadlock-freedom only, schedules may not be serializable",
          "D. Dirty read anomalies will occur"
        ],
        "correct_option": "A",
        "explanation": "Strict 2PL guarantees serializability (and strict schedules). Enforcing a global linear order on lock acquisitions eliminates circular wait, guaranteeing deadlock-freedom."
      }
    ]
  },
  {
    "id": "MCQ-035",
    "title": "B+ Tree Balanced Property Definition",
    "topic": "Indexing & Storage",
    "subtopic": "B+ Tree Balanced Invariants",
    "difficulty": "Easy",
    "source": "GATE CSE 2016 Set 2 | Question: 21 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 31)",
    "source_file": "PYQs/CS_extracted/CS/2016_CS.pdf",
    "source_page": 31,
    "source_qnum": "Q.21",
    "evidence_snippet": "Q.21 B+ Trees are considered BALANCED because (A) the lengths of the paths from the root to all leaf nodes are all equal. (B) the lengths of the paths from the root to all leaf nodes differ from each other by at most 1.",
    "prompt": "B+ Trees are considered BALANCED because:",
    "options": [
      "A. The lengths of the paths from the root to all leaf nodes are all equal",
      "B. The lengths of the paths from the root to all leaf nodes differ by at most 1",
      "C. The number of keys in any two leaf nodes is identical",
      "D. The number of child pointers in all internal nodes is identical"
    ],
    "correct_option": "A",
    "explanation": "A B+ tree is balanced in the strictest sense: every leaf node is located at the exact same depth from the root. Thus, the path length from the root to every leaf node is identical throughout the lifetime of the tree.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital pharmacy uses a B+ tree index to locate medication barcodes. What structural property ensures predictable access latency?",
        "options": [
          "A. Leaf nodes have heights differing by at most 1 like an AVL tree",
          "B. Keys are distributed randomly across levels",
          "C. All leaf nodes have the exact same distance (path length) from the root",
          "D. Internal nodes are binary trees"
        ],
        "correct_option": "C",
        "explanation": "By definition, all leaf nodes in a B+ tree reside at the identical tree depth."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated check clearing index structured as a B+ tree, why is search time guaranteed to be O(log N) for every account?",
        "options": [
          "A. Because every leaf node contains identical balance figures",
          "B. Because the path length from the root to every leaf node is exactly equal",
          "C. Because internal nodes are completely full at all times",
          "D. Because leaf nodes differ in depth by at most 2"
        ],
        "correct_option": "B",
        "explanation": "B+ trees are perfectly height-balanced; all leaf nodes reside at the exact same depth."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why is a B+ tree index on an e-commerce Orders table described as perfectly height-balanced?",
        "options": [
          "A. Because every leaf node resides at the exact same depth from the root node",
          "B. Because left and right subtrees have equal number of keys",
          "C. Because leaf nodes differ in depth by at most 1",
          "D. Because all internal nodes have exactly 2 children"
        ],
        "correct_option": "A",
        "explanation": "In a B+ tree, tree growth occurs exclusively at the root via splitting, ensuring that all leaf nodes are located at the exact same path length (depth) from the root."
      }
    ]
  },
  {
    "id": "MCQ-036",
    "title": "Precedence Graph Topological Ordering for Equivalent Serial Schedule",
    "topic": "Concurrency Control",
    "subtopic": "Precedence Graph & Conflict Serializability",
    "difficulty": "Easy",
    "source": "GATE CSE 2016 Set 2 | Question: 22 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 31)",
    "source_file": "PYQs/CS_extracted/CS/2016_CS.pdf",
    "source_page": 31,
    "source_qnum": "Q.22",
    "evidence_snippet": "Q.22 Suppose a database schedule S involves transactions T1, ..., Tn. Construct the precedence graph of S with vertices representing the transactions and edges representing the conflicts. If S is serializable, which one of the following orderings of the vertices of the precedence graph is guaranteed to yield a serial schedule? (A) Topological order",
    "prompt": "Suppose a database schedule S involves transactions T1, ..., Tn with an acyclic precedence graph (conflict serializable). Which vertex ordering of the precedence graph is guaranteed to produce an equivalent serial schedule?",
    "options": [
      "A. Topological order",
      "B. Depth-first order",
      "C. Breadth-first order",
      "D. Ascending order of transaction IDs"
    ],
    "correct_option": "A",
    "explanation": "When a schedule S is conflict serializable, its precedence graph is a Directed Acyclic Graph (DAG). Any topological sort of this DAG produces a valid serial schedule that is conflict-equivalent to S, because for every conflict edge Ti -> Tj, Ti precedes Tj in the topological ordering.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an intensive care ventilator monitoring database, concurrent sensor read/write operations produce an acyclic conflict graph. Which ordering guarantees an equivalent serial execution?",
        "options": [
          "A. In-order traversal",
          "B. Breadth-first order",
          "C. Topological order",
          "D. Priority queue order"
        ],
        "correct_option": "C",
        "explanation": "A topological order of the precedence graph provides a conflict-equivalent serial schedule."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A banking ledger engine serializes concurrent funds transfers by constructing a transaction dependency graph. If the graph is acyclic, which traversal order yields the equivalent serial execution order?",
        "options": [
          "A. Breadth-first search order",
          "B. Topological order",
          "C. Reverse post-order DFS only",
          "D. Chronological submission order"
        ],
        "correct_option": "B",
        "explanation": "Topological sort on an acyclic conflict graph produces an equivalent serial schedule."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce checkout concurrency log, transactions T1, T2, and T3 produce an acyclic precedence graph with directed edges T1 -> T2 and T2 -> T3. What equivalent serial execution order is guaranteed?",
        "options": [
          "A. T1 followed by T2 followed by T3 (T1, T2, T3)",
          "B. T3, T2, T1",
          "C. T2, T1, T3",
          "D. T3, T1, T2"
        ],
        "correct_option": "A",
        "explanation": "Topological sorting of a Directed Acyclic Graph (DAG) with edges T1 -> T2 -> T3 yields the unique equivalent serial schedule: T1, T2, T3."
      }
    ]
  },
  {
    "id": "MCQ-037",
    "title": "Candidate Key Derivation from Multi-Attribute Functional Dependencies",
    "topic": "Functional Dependencies",
    "subtopic": "Candidate Key Computation",
    "difficulty": "Medium",
    "source": "GATE CSE 2014 Set 1 | Question: 21 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 12)",
    "source_file": "PYQs/CS_extracted/CS/2014_CS.pdf",
    "source_page": 12,
    "source_qnum": "Q.21",
    "evidence_snippet": "Q.21 Consider the relation scheme R = (E, F, G, H, I, J, K, L, M, N) and functional dependencies {{E, F} -> {G}, {F} -> {I, J}, {E, H} -> {K, L}, {K} -> {M}, {L} -> {N}}. What is the key for R? (B) {E, F, H}",
    "prompt": "Consider relation scheme R = (E, F, G, H, I, J, K, L, M, N) and functional dependencies F = { {E, F} -> {G}, {F} -> {I, J}, {E, H} -> {K, L}, {K} -> {M}, {L} -> {N} }. What is the candidate key for R?",
    "options": [
      "A. {E, F, H}",
      "B. {E, F}",
      "C. {E, F, H, K, L}",
      "D. {E}"
    ],
    "correct_option": "A",
    "explanation": "Notice that attributes E, F, and H never appear on the right-hand side of any functional dependency in F. Therefore, E, F, and H must be present in every candidate key.\nComputing closure ({E, F, H})+:\n- From {E, F} -> {G}, we get G.\n- From {F} -> {I, J}, we get I, J.\n- From {E, H} -> {K, L}, we get K, L.\n- From {K} -> {M}, we get M.\n- From {L} -> {N}, we get N.\nThus ({E, F, H})+ = {E, F, G, H, I, J, K, L, M, N} (all attributes).\nSince no subset of {E, F, H} can derive all attributes, {E, F, H} is the unique minimal candidate key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical hospital genomics database R(E, F, G, H, I, J, K, L, M, N) with FDs {{E,F}->G, F->{I,J}, {E,H}->{K,L}, K->M, L->N}, which attribute set is the minimal key?",
        "options": [
          "A. {E, F, G}",
          "B. {E, H, K}",
          "C. {E, F, H}",
          "D. {F, H, L}"
        ],
        "correct_option": "C",
        "explanation": "Closing {E, F, H} yields all 10 attributes; since E, F, H never appear on the RHS, they are indispensable."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking risk database R(E, F, G, H, I, J, K, L, M, N) with FDs {{E,F}->G, F->{I,J}, {E,H}->{K,L}, K->M, L->N}, what is the candidate key?",
        "options": [
          "A. {E, F}",
          "B. {E, F, H}",
          "C. {E, H}",
          "D. {E, F, H, K}"
        ],
        "correct_option": "B",
        "explanation": "Attributes E, F, and H are absent from all dependency RHS sets, and ({E, F, H})+ determines the entire relation."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce marketplace table Listing(SellerID, ItemID, WarehouseID, Commission) has FDs SellerID, ItemID -> WarehouseID and WarehouseID -> Commission. What is the candidate key for Listing?",
        "options": [
          "A. {SellerID, ItemID}",
          "B. {WarehouseID}",
          "C. {SellerID, Commission}",
          "D. {Commission}"
        ],
        "correct_option": "A",
        "explanation": "Attributes SellerID and ItemID do not appear on any RHS, so they must be in every candidate key. {SellerID, ItemID}+ = {SellerID, ItemID, WarehouseID, Commission} = R. Thus {SellerID, ItemID} is the unique minimal candidate key."
      }
    ]
  },
  {
    "id": "MCQ-038",
    "title": "Foreign Key SQL Constraints and Check Assertion Validity",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "Foreign Key Definition & Check Constraints",
    "difficulty": "Medium",
    "source": "GATE CSE 2014 Set 1 | Question: 22 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 12)",
    "source_file": "PYQs/CS_extracted/CS/2014_CS.pdf",
    "source_page": 12,
    "source_qnum": "Q.22",
    "evidence_snippet": "Q.22 Given the following statements: S1: A foreign key declaration can always be replaced by an equivalent check assertion in SQL. S2: Given the table R(a,b,c) where a and b together form the primary key, the following is a valid table definition. CREATE TABLE S (a INTEGER, d INTEGER, e INTEGER, PRIMARY KEY (d), FOREIGN KEY (a) references R). Which one of the following statements is CORRECT? (D) Both S1 and S2 are FALSE.",
    "prompt": "Consider the statements:\nS1: A foreign key declaration can always be replaced by an equivalent CHECK constraint in standard SQL.\nS2: Given table R(a, b, c) where (a, b) together form the primary key, 'FOREIGN KEY (a) REFERENCES R' is a valid table definition.\nWhich one of the following is CORRECT?",
    "options": [
      "A. Both S1 and S2 are FALSE",
      "B. S1 is TRUE and S2 is FALSE",
      "C. S1 is FALSE and S2 is TRUE",
      "D. Both S1 and S2 are TRUE"
    ],
    "correct_option": "A",
    "explanation": "1. S1 is FALSE: In standard SQL, CHECK constraints cannot query other tables (no subqueries allowed in CHECK in standard relational engines), so they cannot replace foreign key referential integrity.\n2. S2 is FALSE: A foreign key must reference a candidate key or primary key of the target table. Here, (a, b) is the composite primary key; referencing only attribute 'a' (a proper subset) violates SQL standards and is rejected.\nTherefore, both S1 and S2 are FALSE.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR database developer asserts: (S1) CHECK constraints can enforce foreign keys across patient tables; (S2) table S can reference partial primary key (a) of R(a, b). What is the validity of these assertions?",
        "options": [
          "A. S1 is FALSE and S2 is TRUE",
          "B. Both S1 and S2 are TRUE",
          "C. Both S1 and S2 are FALSE",
          "D. S1 is TRUE and S2 is FALSE"
        ],
        "correct_option": "C",
        "explanation": "Standard SQL foreign keys must reference a full candidate key, and CHECK constraints cannot enforce inter-relation referential integrity."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking compliance system: S1 claims a CHECK constraint can always replace foreign keys; S2 claims a foreign key can reference a partial primary key. Which statement is correct?",
        "options": [
          "A. S1 is TRUE and S2 is FALSE",
          "B. Both S1 and S2 are FALSE",
          "C. S1 is FALSE and S2 is TRUE",
          "D. Both S1 and S2 are TRUE"
        ],
        "correct_option": "B",
        "explanation": "CHECK constraints cannot reference other relations, and foreign keys cannot reference a proper subset of a composite primary key."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In SQL DDL for an e-commerce catalog, table Product(Price NUMERIC, Discount NUMERIC) specifies constraint CHECK (Price >= Discount AND Discount >= 0). When is this constraint evaluated?",
        "options": [
          "A. Automatically upon every INSERT and UPDATE operation affecting Price or Discount",
          "B. Only when the database server is rebooted",
          "C. Only when a SELECT query is executed",
          "D. Once per month during index defragmentation"
        ],
        "correct_option": "A",
        "explanation": "SQL table CHECK constraints are evaluated by the DBMS engine whenever rows are inserted or updated, rejecting any modification that violates the boolean predicate."
      }
    ]
  },
  {
    "id": "MCQ-039",
    "title": "Conflict Serializability Testing on Concurrent Schedules",
    "topic": "Concurrency Control",
    "subtopic": "Precedence Graph Cycle Detection",
    "difficulty": "Medium",
    "source": "GATE CSE 2014 Set 1 | Question: 29 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 14)",
    "source_file": "PYQs/CS_extracted/CS/2014_CS.pdf",
    "source_page": 14,
    "source_qnum": "Q.29",
    "evidence_snippet": "Q.29 Consider the following four schedules due to three transactions using read and write on a data item x, denoted by r(x) and w(x) respectively. Which one of them is conflict serializable? (D) r2(x); w2(x); r3(x); r1(x); w1(x)",
    "prompt": "Consider four schedules of three transactions operating on data item x. Which one of them is conflict serializable?",
    "options": [
      "A. r2(x); w2(x); r3(x); r1(x); w1(x)",
      "B. r1(x); r2(x); w1(x); r3(x); w2(x)",
      "C. r2(x); r1(x); w2(x); r3(x); w1(x)",
      "D. r3(x); r2(x); r1(x); w2(x); w1(x)"
    ],
    "correct_option": "A",
    "explanation": "Analyze schedule (A): r2(x); w2(x); r3(x); r1(x); w1(x):\n- Conflict w2(x) before r3(x) -> edge T2 -> T3\n- Conflict w2(x) before r1(x) -> edge T2 -> T1\n- Conflict w2(x) before w1(x) -> edge T2 -> T1\n- Conflict r3(x) before w1(x) -> edge T3 -> T1\nThe edges in the precedence graph are T2 -> T3, T2 -> T1, and T3 -> T1. This graph is completely acyclic (topological order: T2, T3, T1).\nIn options B, C, and D, circular edges exist between T1 and T2 (e.g. T1 -> T2 and T2 -> T1), creating cycles.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR audit log records concurrent clinical updates on medication x. Which schedule has an acyclic precedence graph?",
        "options": [
          "A. r1(x); r2(x); w1(x); r3(x); w2(x)",
          "B. r3(x); r2(x); r1(x); w2(x); w1(x)",
          "C. r2(x); w2(x); r3(x); r1(x); w1(x)",
          "D. r2(x); r1(x); w2(x); r3(x); w1(x)"
        ],
        "correct_option": "C",
        "explanation": "T2 completes its writes before T3 and T1 read and write, producing edges T2->T3 and T3->T1 with no cycles."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated securities transaction log, which sequence of concurrent operations is conflict serializable without deadlock or dependency cycle?",
        "options": [
          "A. r1(x); r2(x); w1(x); r3(x); w2(x)",
          "B. r2(x); w2(x); r3(x); r1(x); w1(x)",
          "C. r2(x); r1(x); w2(x); r3(x); w1(x)",
          "D. r3(x); r2(x); r1(x); w2(x); w1(x)"
        ],
        "correct_option": "B",
        "explanation": "Precedence graph for r2; w2; r3; r1; w1 has edges T2->T3 and T3->T1 with zero back edges, making it acyclic and serializable."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a flash sale, schedule S contains operations: T1: Read(Stock); T2: Write(Stock); T1: Write(Stock). Why is schedule S NOT conflict serializable?",
        "options": [
          "A. Because the conflicting operations between T1 and T2 form a directed cycle: T1 -> T2 (Read-Write conflict) and T2 -> T1 (Write-Write conflict)",
          "B. Because T1 and T2 read the same variable",
          "C. Because transactions are not allowed to update stock",
          "D. Because T1 did not commit before T2 started"
        ],
        "correct_option": "A",
        "explanation": "T1: Read(Stock) precedes T2: Write(Stock), creating edge T1 -> T2. T2: Write(Stock) precedes T1: Write(Stock), creating edge T2 -> T1. The cycle T1 <-> T2 violates conflict serializability."
      }
    ]
  },
  {
    "id": "MCQ-040",
    "title": "Minimal Cover and Two-Attribute Relation Normal Form Invariants",
    "topic": "Functional Dependencies",
    "subtopic": "Minimal Cover & Binary Relation Normal Form",
    "difficulty": "Medium",
    "source": "GATE CSE 2014 Set 1 | Question: 30 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 14)",
    "source_file": "PYQs/CS_extracted/CS/2014_CS.pdf",
    "source_page": 14,
    "source_qnum": "Q.30",
    "evidence_snippet": "Q.30 Given the following two statements: S1: Every table with two single-valued attributes is in 1NF, 2NF, 3NF and BCNF. S2: AB→C, D→E, E→C is a minimal cover for the set of functional dependencies AB→C, D→E, AB→E, E→C. Which one of the following is CORRECT? (A) S1 is TRUE and S2 is FALSE.",
    "prompt": "Consider two statements:\nS1: Every relational table with two single-valued attributes is in 1NF, 2NF, 3NF, and BCNF.\nS2: { AB -> C, D -> E, E -> C } is a minimal cover for { AB -> C, D -> E, AB -> E, E -> C }.\nWhich one of the following is CORRECT?",
    "options": [
      "A. S1 is TRUE and S2 is FALSE",
      "B. Both S1 and S2 are TRUE",
      "C. S1 is FALSE and S2 is TRUE",
      "D. Both S1 and S2 are FALSE"
    ],
    "correct_option": "A",
    "explanation": "1. S1 is TRUE: Any binary relation R(A, B) with single-valued attributes cannot have partial or transitive dependencies; either A->B (A is key), B->A (B is key), or AB is key. In all cases, every non-trivial FD has a superkey on the LHS, satisfying BCNF (and thus 3NF, 2NF, 1NF).\n2. S2 is FALSE: In the original set, (AB)+ under {AB->C, D->E, AB->E, E->C} includes E. But under {AB->C, D->E, E->C}, (AB)+ = {A, B, C}, so AB->E cannot be derived. Therefore, removing AB->E changed the closure, meaning {AB->C, D->E, E->C} is NOT equivalent and cannot be a minimal cover.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR database schema audit evaluates: (S1) All two-attribute tables meet BCNF; (S2) {AB->C, D->E, E->C} is a minimal cover for {AB->C, D->E, AB->E, E->C}. Which is correct?",
        "options": [
          "A. Both S1 and S2 are FALSE",
          "B. S1 is FALSE and S2 is TRUE",
          "C. S1 is TRUE and S2 is FALSE",
          "D. Both S1 and S2 are TRUE"
        ],
        "correct_option": "C",
        "explanation": "Binary tables are guaranteed BCNF; dropping AB->E is invalid because AB->E is not redundant."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking risk framework: S1 asserts any two-column relation is in BCNF; S2 asserts {AB->C, D->E, E->C} is a minimal cover for {AB->C, D->E, AB->E, E->C}. What is the truth value?",
        "options": [
          "A. Both S1 and S2 are TRUE",
          "B. S1 is TRUE and S2 is FALSE",
          "C. S1 is FALSE and S2 is TRUE",
          "D. Both S1 and S2 are FALSE"
        ],
        "correct_option": "B",
        "explanation": "Two-attribute relations are always in BCNF; discarding AB->E loses the dependency AB->E because D->E cannot fire from AB."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce table with only two attributes Vendor_Zip(VendorID, ZipCode), in which normal form is the relation guaranteed to be?",
        "options": [
          "A. Always in at least BCNF (and 3NF, 2NF, 1NF)",
          "B. Only in 1NF",
          "C. Never in BCNF",
          "D. Only in 2NF"
        ],
        "correct_option": "A",
        "explanation": "Any binary relation (with exactly two attributes) is guaranteed to be in BCNF. Non-trivial FDs can only be A -> B or B -> A, in which case the determinant is a candidate key."
      }
    ]
  },
  {
    "id": "MCQ-041",
    "title": "SQL Pairwise Comparison Subquery with GROUP BY and JOIN",
    "topic": "SQL & Query Processing",
    "subtopic": "Pairwise Subqueries & Join Semantics",
    "difficulty": "Hard",
    "source": "GATE CSE 2014 Set 1 | Question: 54 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 21)",
    "source_file": "PYQs/CS_extracted/CS/2014_CS.pdf",
    "source_page": 21,
    "source_qnum": "Q.54",
    "evidence_snippet": "Q.54 Given the following schema: employees(emp-id, first-name, last-name, hire-date, dept-id, salary), departments(dept-id, dept-name, manager-id, location-id). You want to display last names and hire dates of all latest hires in departments in location 1700: SELECT last-name, hire-date FROM employees WHERE (dept-id, hire-date) IN (SELECT dept-id, MAX(hire-date) FROM employees JOIN departments USING(dept-id) WHERE location-id = 1700 GROUP BY dept-id); What is the outcome? (B) It executes and gives the correct result.",
    "prompt": "Consider tables employees(emp_id, first_name, last_name, hire_date, dept_id, salary) and departments(dept_id, dept_name, manager_id, location_id). To display the last names and hire dates of all latest hires in their departments in location 1700, the following query is executed:\nSELECT last_name, hire_date FROM employees WHERE (dept_id, hire_date) IN (SELECT dept_id, MAX(hire_date) FROM employees JOIN departments USING(dept_id) WHERE location_id = 1700 GROUP BY dept_id);\nWhat is the outcome?",
    "options": [
      "A. It executes and gives the correct result",
      "B. It executes but does not give the correct result",
      "C. It generates an error because pairwise comparison is not allowed",
      "D. It generates an error because GROUP BY cannot be used in a subquery"
    ],
    "correct_option": "A",
    "explanation": "Standard SQL (SQL-92 and later) fully supports multi-column (pairwise) row value constructors with the IN operator: `(dept_id, hire_date) IN (SELECT ...)`. The subquery joins employees with departments, filters by location_id = 1700, and groups by dept_id to return the pair (dept_id, MAX(hire_date)) for each department. The outer query matches employees whose department and hire date match these latest hires. It executes cleanly and returns the correct result.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR clinical lab system: Lab_Results(test_id, panel_id, recorded_time, value) and Panels(panel_id, ward_id). The query uses `WHERE (panel_id, recorded_time) IN (SELECT panel_id, MAX(recorded_time) ... GROUP BY panel_id)`. What happens?",
        "options": [
          "A. It throws a syntax error on pairwise tuple matching",
          "B. It returns all lab results regardless of timestamp",
          "C. It executes and correctly returns the latest lab results",
          "D. GROUP BY in subqueries is restricted to single columns"
        ],
        "correct_option": "C",
        "explanation": "Row value constructors `(a, b) IN (SELECT a, max(b) ...)` are valid SQL and correctly identify latest records."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an investment bank portfolio audit: Positions(pos_id, desk_id, tx_date, amount) and Desks(desk_id, region_id). A query matches `(desk_id, tx_date) IN (SELECT desk_id, MAX(tx_date) ... WHERE region_id = 100 GROUP BY desk_id)`. What is the outcome?",
        "options": [
          "A. It fails due to invalid row constructor syntax",
          "B. It executes and gives the correct result",
          "C. It executes but returns incorrect desks",
          "D. Subqueries with GROUP BY cannot join tables"
        ],
        "correct_option": "B",
        "explanation": "Multi-column IN predicates with grouped subqueries are standard SQL and evaluate correctly."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce query evaluates: SELECT CustomerID FROM Orders GROUP BY CustomerID HAVING SUM(TotalAmount) > (SELECT AVG(TotalAmount) FROM Orders). What does this query return?",
        "options": [
          "A. Customers whose total lifetime spending exceeds the average order value across all individual orders",
          "B. All orders whose amount is above average",
          "C. Customers who placed zero orders",
          "D. A syntax error because HAVING cannot contain subqueries"
        ],
        "correct_option": "A",
        "explanation": "The scalar subquery computes the global average of TotalAmount across all orders. The outer query groups orders by CustomerID and filters for customers whose total spending (SUM) exceeds that average."
      }
    ]
  },
  {
    "id": "MCQ-042",
    "title": "SQL Subquery Multiplicity and Duplicate Preservation",
    "topic": "SQL & Query Processing",
    "subtopic": "Subquery Equivalence & Multiset Semantics",
    "difficulty": "Medium",
    "source": "GATE CSE 2014 Set 2 | Question: 54 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 43)",
    "source_file": "PYQs/CS_extracted/CS/2014_CS.pdf",
    "source_page": 43,
    "source_qnum": "Q.54",
    "evidence_snippet": "Q.54 SQL allows duplicate tuples in relations, and correspondingly defines the multiplicity of tuples in the result of joins. Which one of the following queries always gives the same answer as the nested query shown below: select * from R where a in (select S.a from S) (C) select R.* from R,(select distinct a from S) as S1 where R.a=S1.a",
    "prompt": "SQL operates under multiset (bag) semantics allowing duplicate tuples. Which of the following queries ALWAYS produces the exact same answer (including tuple multiplicity) as:\nSELECT * FROM R WHERE a IN (SELECT S.a FROM S)?",
    "options": [
      "A. SELECT R.* FROM R, (SELECT DISTINCT a FROM S) AS S1 WHERE R.a = S1.a",
      "B. SELECT R.* FROM R, S WHERE R.a = S.a",
      "C. SELECT DISTINCT R.* FROM R, S WHERE R.a = S.a",
      "D. SELECT R.* FROM R, S WHERE R.a = S.a AND is unique R"
    ],
    "correct_option": "A",
    "explanation": "In `WHERE a IN (SELECT S.a FROM S)`:\n- Each tuple in R is output as many times as it appears in R, provided its 'a' value exists in S (duplicates in S do NOT multiply R tuples).\n- Query (B) multiplies each R tuple by the count of matching 'a' values in S.\n- Query (C) collapses genuine duplicate tuples in R via DISTINCT R.*.\n- Query (A) joins R with `(SELECT DISTINCT a FROM S)`, ensuring each matching 'a' appears exactly once from S, thereby preserving the exact original multiplicity of tuples in R.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR medication table Prescriptions(R) matching against an Formulary(S), which query preserves exact prescription counts as `WHERE drug_id IN (SELECT drug_id FROM S)`?",
        "options": [
          "A. SELECT R.* FROM R, S WHERE R.drug_id = S.drug_id",
          "B. SELECT DISTINCT R.* FROM R, S WHERE R.drug_id = S.drug_id",
          "C. SELECT R.* FROM R, (SELECT DISTINCT drug_id FROM S) AS S1 WHERE R.drug_id = S1.drug_id",
          "D. SELECT R.* FROM R WHERE EXISTS (SELECT * FROM S)"
        ],
        "correct_option": "C",
        "explanation": "Eliminating duplicates from S before joining guarantees that each R tuple matches at most once."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial ledger with duplicate transaction rows in R, which join query reproduces `SELECT * FROM R WHERE acc_id IN (SELECT acc_id FROM S)` without artificial row multiplication?",
        "options": [
          "A. SELECT R.* FROM R, S WHERE R.acc_id = S.acc_id",
          "B. SELECT R.* FROM R, (SELECT DISTINCT acc_id FROM S) AS S1 WHERE R.acc_id = S1.acc_id",
          "C. SELECT DISTINCT R.* FROM R, S WHERE R.acc_id = S.acc_id",
          "D. SELECT R.* FROM R NATURAL JOIN S"
        ],
        "correct_option": "B",
        "explanation": "Joining with distinct keys of S prevents cross-product duplication while retaining R's duplicates."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In SQL, what is the difference between UNION and UNION ALL when combining order customer IDs from Online_Orders and InStore_Orders?",
        "options": [
          "A. UNION eliminates duplicate customer IDs via sorting/hashing, whereas UNION ALL retains all duplicates without deduplication",
          "B. UNION ALL eliminates duplicates, while UNION retains them",
          "C. UNION can only combine numeric columns",
          "D. UNION ALL converts NULL values into zero"
        ],
        "correct_option": "A",
        "explanation": "Standard SQL specifies that UNION removes duplicate rows from the final result set, while UNION ALL concatenates the multiset of tuples directly, preserving all duplicate occurrences."
      }
    ]
  },
  {
    "id": "MCQ-043",
    "title": "Clustered Index Physical Data File Organization",
    "topic": "Indexing & Storage",
    "subtopic": "Clustered vs Unclustered Indexing",
    "difficulty": "Easy",
    "source": "GATE CSE 2013 | Question: 15 (PYQs/CS_extracted/CS/2013_CS.pdf, Page 5)",
    "source_file": "PYQs/CS_extracted/CS/2013_CS.pdf",
    "source_page": 5,
    "source_qnum": "Q.15",
    "evidence_snippet": "Q.15 An index is clustered, if (A) it is on a set of fields that form a candidate key. (B) it is on a set of fields that include the primary key. (C) the data records of the file are organized in the same order as the data entries of the index. (D) the data records of the file are organized not in the same order as the data entries of the index.",
    "prompt": "An index is defined as a clustered index if:",
    "options": [
      "A. The data records of the file are physically organized in the same order as the data entries of the index",
      "B. It is created on a set of fields that form a candidate key",
      "C. It is created on a set of fields that include the primary key",
      "D. The data records of the file are organized in an order different from the index entries"
    ],
    "correct_option": "A",
    "explanation": "A clustered index is one where the physical storage order of tuples in the data file matches the sequential search key order of index entries. Because data records can only be physically stored in one sequential order on disk, a table can have at most ONE clustered index.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR medical imaging archive creates a clustered index on Patient_Scan_Time. What physical guarantee does this provide?",
        "options": [
          "A. Scan time is guaranteed to be unique across all patients",
          "B. Scan images are stored in-memory without secondary indexing",
          "C. The scan records on disk are physically sorted in the identical order as the index entries",
          "D. Multiple clustered indexes can be maintained simultaneously"
        ],
        "correct_option": "C",
        "explanation": "A clustered index aligns the physical file records with the logical ordering of the index."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a high-throughput bank settlement database, why can a transaction table have only one clustered index?",
        "options": [
          "A. Because transactions permit only one primary key constraint",
          "B. Because table data records can be physically organized on disk in only one sorted order",
          "C. Because clustered indexes require exclusive locks",
          "D. Because secondary indexes must be B-trees"
        ],
        "correct_option": "B",
        "explanation": "Clustering dictates physical block placement on storage, which can only follow a single order."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce database administrator creates a clustered index on Orders(OrderDate). How does this impact the physical storage of tuples in the data file?",
        "options": [
          "A. The actual data records on disk are physically stored and sorted in the sequence of the clustered index key (OrderDate)",
          "B. A separate copy of the entire table is created for every employee",
          "C. Tuples are scattered randomly across disk blocks",
          "D. The database can create up to 10 clustered indexes on the same table"
        ],
        "correct_option": "A",
        "explanation": "A clustered index defines the physical order of data rows on disk. Consequently, a table can possess at most one clustered index, and its tuples are physically organized in order of the index key."
      }
    ]
  },
  {
    "id": "MCQ-044",
    "title": "Relational Query Equivalence Across SQL, RA, TRC, and DRC",
    "topic": "Relational Algebra",
    "subtopic": "Formal Query Language Equivalence",
    "difficulty": "Hard",
    "source": "GATE CSE 2013 | Question: 35 (PYQs/CS_extracted/CS/2013_CS.pdf, Page 9)",
    "source_file": "PYQs/CS_extracted/CS/2013_CS.pdf",
    "source_page": 9,
    "source_qnum": "Q.35",
    "evidence_snippet": "Q.35 Consider relational schema: Students(rollno, sname), Courses(courseno, cname), Registration(rollno, courseno, percent). Which of the following queries are equivalent to: “Find distinct names of all students who score more than 90% in course 107”? (I) SQL (II) RA (III) TRC (IV) DRC. (A) I, II, III and IV",
    "prompt": "Consider schema Students(rollno, sname), Courses(courseno, cname), Registration(rollno, courseno, percent). Query: 'Find distinct names of all students scoring > 90% in course 107'.\nI. SQL: SELECT DISTINCT S.sname FROM Students S, Registration R WHERE R.rollno=S.rollno AND R.courseno=107 AND R.percent > 90\nII. Relational Algebra: ∏_sname ( σ_{courseno=107 ∧ percent>90} (Registration ⨝ Students) )\nIII. TRC: { T | ∃S∈Students ∃R∈Registration ( S.rollno=R.rollno ∧ R.courseno=107 ∧ R.percent>90 ∧ T.sname=S.sname ) }\nIV. DRC: { ⟨SN⟩ | ∃SR ∃RP ( ⟨SR, SN⟩∈Students ∧ ⟨SR, 107, RP⟩∈Registration ∧ RP>90 ) }\nWhich of these queries correctly express the requirement?",
    "options": [
      "A. I, II, III, and IV",
      "B. I, II, and III only",
      "C. I, II, and IV only",
      "D. II, III, and IV only"
    ],
    "correct_option": "A",
    "explanation": "All four formulations are standard and mathematically equivalent expressions of the English query:\n- (I) SQL joins on rollno, filters courseno=107 and percent>90, and projects distinct sname.\n- (II) RA computes natural join, selects on conditions, and projects sname.\n- (III) TRC binds existential tuple variables S and R with equality and predicates.\n- (IV) DRC binds domain variables SR and RP, matching on rollno and asserting RP > 90.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR data pipeline searches for distinct oncology patients diagnosed with Stage IV lymphoma across SQL, RA, TRC, and DRC formulations. How many are equivalent?",
        "options": [
          "A. Only the SQL and Relational Algebra expressions",
          "B. Only TRC and DRC",
          "C. All four expressions are logically equivalent",
          "D. Only the SQL query"
        ],
        "correct_option": "C",
        "explanation": "Codd's theorem establishes the expressive equivalence of relational algebra, TRC, DRC, and declarative SQL."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated finance compliance engine, a query retrieves distinct traders who executed trades exceeding $1M in Desk 107 expressed across SQL, RA, TRC, and DRC. Which formulations are valid?",
        "options": [
          "A. Only SQL and Relational Algebra",
          "B. All four formulations (SQL, RA, TRC, DRC) are valid and equivalent",
          "C. Only SQL and TRC",
          "D. Only Relational Algebra and DRC"
        ],
        "correct_option": "B",
        "explanation": "SQL, RA, TRC, and DRC are relationally complete and express the join-select-project operation identically."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Which theoretical foundation establishes that basic Relational Algebra, Tuple Relational Calculus (TRC), and Domain Relational Calculus (DRC) have identical expressive query power?",
        "options": [
          "A. Codd's Equivalence Theorem (Relational Completeness)",
          "B. Armstrong's Axioms",
          "C. CAP Theorem",
          "D. Amdahl's Law"
        ],
        "correct_option": "A",
        "explanation": "Codd's Theorem proves that relational algebra and domain-independent tuple/domain relational calculus are expressively equivalent, defining the benchmark for relational completeness."
      }
    ]
  },
  {
    "id": "MCQ-045",
    "title": "Relational Normal Form Hierarchy: BCNF Subsumption of 3NF",
    "topic": "Normalization & Functional Dependencies",
    "subtopic": "Normal Form Hierarchy & Containment",
    "difficulty": "Easy",
    "source": "GATE CSE 2012 | Question: 2 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 2)",
    "source_file": "PYQs/CS_extracted/CS/2012_CS.pdf",
    "source_page": 2,
    "source_qnum": "Q.2",
    "evidence_snippet": "Q.2 Which of the following is TRUE? (A) Every relation in 3NF is also in BCNF (B) A relation R is in 3NF if every non-prime attribute of R is fully functionally dependent on every key of R (C) Every relation in BCNF is also in 3NF (D) No relation can be in both BCNF and 3NF",
    "prompt": "Which of the following statements regarding database normal forms is TRUE?",
    "options": [
      "A. Every relation in BCNF is also in 3NF",
      "B. Every relation in 3NF is also in BCNF",
      "C. A relation is in 3NF if every non-prime attribute is fully functionally dependent on every key",
      "D. No relation can be in both BCNF and 3NF simultaneously"
    ],
    "correct_option": "A",
    "explanation": "The normal form inclusion hierarchy is: 5NF ⊂ 4NF ⊂ BCNF ⊂ 3NF ⊂ 2NF ⊂ 1NF.\nSince BCNF imposes a strictly stronger constraint than 3NF (BCNF requires every non-trivial X -> Y to have X as a superkey, whereas 3NF also allows Y to be a prime attribute), every relation in BCNF is guaranteed to be in 3NF.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR database audit checks schema normalization tiers. Which statement is universally valid?",
        "options": [
          "A. Every clinical table in 3NF is automatically in BCNF",
          "B. Tables in 3NF cannot be in 2NF",
          "C. Every clinical table in BCNF is also in 3NF",
          "D. BCNF permits non-trivial dependencies on non-superkeys"
        ],
        "correct_option": "C",
        "explanation": "BCNF is strictly more restrictive than 3NF; hence BCNF ⊂ 3NF holds universally."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking architecture standard, which schema containment rule is mathematically guaranteed?",
        "options": [
          "A. Every ledger relation in 3NF satisfies BCNF",
          "B. Every ledger relation satisfying BCNF is guaranteed to satisfy 3NF",
          "C. 3NF and BCNF are mutually disjoint sets of schemas",
          "D. 2NF guarantees absence of transitive dependencies"
        ],
        "correct_option": "B",
        "explanation": "BCNF is a strict subset of 3NF; meeting BCNF inherently satisfies 3NF."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In relational normalization theory, what is the relationship between Boyce-Codd Normal Form (BCNF) and Third Normal Form (3NF) for an e-commerce schema?",
        "options": [
          "A. Every relation that satisfies BCNF is guaranteed to satisfy 3NF (BCNF ⊂ 3NF)",
          "B. Every relation that satisfies 3NF is guaranteed to satisfy BCNF",
          "C. 3NF and BCNF are mutually exclusive normal forms",
          "D. BCNF permits transitive dependencies that 3NF prohibits"
        ],
        "correct_option": "A",
        "explanation": "BCNF is a stricter normal form than 3NF. Every relation in BCNF is inherently in 3NF, but not every relation in 3NF satisfies BCNF."
      }
    ]
  },
  {
    "id": "MCQ-046",
    "title": "Relational Model Atomicity vs ER Multivalued Attributes",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "Relational Model Tuple Invariants",
    "difficulty": "Easy",
    "source": "GATE CSE 2012 | Question: 14 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 4)",
    "source_file": "PYQs/CS_extracted/CS/2012_CS.pdf",
    "source_page": 4,
    "source_qnum": "Q.14",
    "evidence_snippet": "Q.14 Given the basic ER and relational models, which of the following is INCORRECT? (A) An attribute of an entity can have more than one value (B) An attribute of an entity can be composite (C) In a row of a relational table, an attribute can have more than one value (D) In a row of a relational table, an attribute can have exactly one value or a NULL value",
    "prompt": "Given the basic ER and relational models, which of the following statements is INCORRECT?",
    "options": [
      "A. In a row of a relational table, an attribute can have more than one value",
      "B. An attribute of an entity in an ER model can have more than one value",
      "C. An attribute of an entity in an ER model can be composite",
      "D. In a row of a relational table, an attribute can have exactly one value or a NULL value"
    ],
    "correct_option": "A",
    "explanation": "In the formal relational model, First Normal Form (1NF) is built into the fundamental definition of a relation: every cell in a relational tuple must contain strictly an atomic (single) value or a NULL value. An attribute in a relational row CANNOT contain multiple values (sets, lists, arrays). In contrast, the conceptual ER model explicitly supports multivalued attributes (e.g., phone numbers).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR medical informatics student compares ER diagrams with relational tables. Which statement is FALSE?",
        "options": [
          "A. In an ER model, an entity attribute can be composite (e.g., Street, City)",
          "B. In an ER model, an entity attribute can be multivalued (e.g., Allergies)",
          "C. In a row of a relational table, an attribute can store multiple values simultaneously",
          "D. In a relational table row, an attribute must be atomic or NULL"
        ],
        "correct_option": "C",
        "explanation": "Relational tables enforce atomicity; storing multiple values in a single tuple cell violates relational foundations."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial compliance audit comparing conceptual ER models against PostgreSQL relational tables, which statement is INCORRECT?",
        "options": [
          "A. An ER entity can define multivalued phone numbers",
          "B. A cell in a relational ledger row can hold a set of multiple values",
          "C. An ER entity can define composite name fields",
          "D. A relational table column can contain a single scalar or NULL"
        ],
        "correct_option": "B",
        "explanation": "Relational model rows must contain strictly atomic values per cell; multi-valued attributes are prohibited."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an ER diagram for an e-commerce store, Product has a multi-valued attribute Image_URLs. How must this be represented when mapped into the relational model?",
        "options": [
          "A. By creating a separate relation Product_Images(ProductID, Image_URL) where each URL is stored in a separate tuple",
          "B. By storing all URLs as a comma-delimited string in a single cell",
          "C. By creating 100 optional columns URL1, URL2... in the Product table",
          "D. Relational databases cannot represent multi-valued attributes"
        ],
        "correct_option": "A",
        "explanation": "In the relational model, all cell values must be atomic (1NF). Multivalued attributes from an ER model are mapped into a separate relation containing the primary key of the entity and the attribute value."
      }
    ]
  },
  {
    "id": "MCQ-047",
    "title": "SQL HAVING Clause Without GROUP BY and Projection Invariants",
    "topic": "SQL & Query Processing",
    "subtopic": "HAVING Clause and Projection Rules",
    "difficulty": "Medium",
    "source": "GATE CSE 2012 | Question: 15 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 4)",
    "source_file": "PYQs/CS_extracted/CS/2012_CS.pdf",
    "source_page": 4,
    "source_qnum": "Q.15",
    "evidence_snippet": "Q.15 Which of the following statements are TRUE about an SQL query? P : An SQL query can contain a HAVING clause even if it does not have a GROUP BY clause. Q : An SQL query can contain a HAVING clause only if it has a GROUP BY clause. R : All attributes used in the GROUP BY clause must appear in the SELECT clause. S : Not all attributes used in the GROUP BY clause need to appear in the SELECT clause. (B) P and S",
    "prompt": "Consider the following statements about an SQL query:\nP: An SQL query can contain a HAVING clause even if it does not have a GROUP BY clause.\nQ: An SQL query can contain a HAVING clause only if it has a GROUP BY clause.\nR: All attributes used in the GROUP BY clause must appear in the SELECT clause.\nS: Not all attributes used in the GROUP BY clause need to appear in the SELECT clause.\nWhich statements are TRUE?",
    "options": [
      "A. P and S",
      "B. P and R",
      "C. Q and R",
      "D. Q and S"
    ],
    "correct_option": "A",
    "explanation": "1. Statement P is TRUE: In standard SQL, a HAVING clause can be applied to an entire table without a GROUP BY clause (treating the whole table as a single group, e.g., `SELECT AVG(salary) FROM emp HAVING COUNT(*) > 10`).\n2. Statement S is TRUE: Attributes in the GROUP BY clause do NOT have to appear in the SELECT projection list (e.g., `SELECT dept_id FROM emp GROUP BY dept_id, region` is completely valid).\nThus, P and S are TRUE.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR database administrator reviews clinical reporting SQL queries. Which two assertions are TRUE?",
        "options": [
          "A. Q and R",
          "B. P and R",
          "C. P and S (Queries can use HAVING without GROUP BY, and GROUP BY columns need not appear in SELECT)",
          "D. Q and S"
        ],
        "correct_option": "C",
        "explanation": "Standard SQL allows HAVING without GROUP BY on global aggregates, and SELECT need not include all GROUP BY attributes."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking SQL optimization engine, which statements regarding grouping and aggregation are TRUE?",
        "options": [
          "A. P and R",
          "B. P and S (HAVING is legal without GROUP BY; GROUP BY attributes need not be projected)",
          "C. Q and R",
          "D. Q and S"
        ],
        "correct_option": "B",
        "explanation": "HAVING filters aggregate groups even across the whole table without GROUP BY, and projection does not require all grouping keys."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce database, is the query SELECT COUNT(*) FROM Orders HAVING AVG(TotalAmount) > 100 valid SQL, and what does it do?",
        "options": [
          "A. It is valid SQL: it treats the entire table as a single group, evaluating HAVING against the global average and returning the count if average > 100",
          "B. It is invalid SQL because HAVING cannot be used without an explicit GROUP BY clause",
          "C. It produces an infinite loop",
          "D. It deletes all orders with TotalAmount <= 100"
        ],
        "correct_option": "A",
        "explanation": "SQL standard allows HAVING without GROUP BY. When omitted, the entire table constitutes a single group. If the condition in HAVING is met, the aggregate result is returned; otherwise, an empty result set is returned."
      }
    ]
  },
  {
    "id": "MCQ-048",
    "title": "Foreign Key Set Difference Invariant Under Referential Integrity",
    "topic": "Relational Model & Integrity Constraints",
    "subtopic": "Foreign Key Inclusion Invariants",
    "difficulty": "Medium",
    "source": "GATE CSE 2012 | Question: 43 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 10)",
    "source_file": "PYQs/CS_extracted/CS/2012_CS.pdf",
    "source_page": 10,
    "source_qnum": "Q.43",
    "evidence_snippet": "Q.43 Suppose R1(A, B) and R2(C, D) are two relation schemas. Let r1 and r2 be corresponding instances. B is a foreign key that refers to C in R2. If data in r1 and r2 satisfy referential integrity constraints, which of the following is ALWAYS TRUE? (A) ∏_B(r1) − ∏_C(r2) = ∅",
    "prompt": "Suppose R1(A, B) and R2(C, D) are relation schemas, and r1, r2 are their instances. Attribute B in R1 is a foreign key referencing primary key C in R2. Assuming referential integrity is satisfied, which of the following is ALWAYS TRUE?",
    "options": [
      "A. ∏_B (r1) − ∏_C (r2) = ∅",
      "B. ∏_C (r2) − ∏_B (r1) = ∅",
      "C. ∏_B (r1) = ∏_C (r2)",
      "D. ∏_B (r1) − ∏_C (r2) ≠ ∅"
    ],
    "correct_option": "A",
    "explanation": "Referential integrity dictates that every foreign key value present in r1 must exist as a valid primary key value in r2 (i.e., ∏_B(r1) ⊆ ∏_C(r2)). Therefore, subtracting ∏_C(r2) from ∏_B(r1) removes all elements, leaving the empty set ∅: ∏_B(r1) − ∏_C(r2) = ∅.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR system, Prescriptions(rx_id, patient_id) references Patients(patient_id). Under referential integrity, which condition is guaranteed?",
        "options": [
          "A. ∏_patient_id (Patients) − ∏_patient_id (Prescriptions) = ∅",
          "B. ∏_patient_id (Prescriptions) = ∏_patient_id (Patients)",
          "C. ∏_patient_id (Prescriptions) − ∏_patient_id (Patients) = ∅",
          "D. ∏_patient_id (Prescriptions) ∪ ∏_patient_id (Patients) = ∅"
        ],
        "correct_option": "C",
        "explanation": "Every referencing patient_id must exist in Patients, so subtracting parent keys from child keys yields the empty set."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial ledger, Transactions(tx_id, acc_id) has foreign key acc_id referencing Accounts(acc_id). Under referential integrity, which set theoretic equation always holds?",
        "options": [
          "A. ∏_acc_id (Accounts) − ∏_acc_id (Transactions) = ∅",
          "B. ∏_acc_id (Transactions) − ∏_acc_id (Accounts) = ∅",
          "C. ∏_acc_id (Transactions) = ∏_acc_id (Accounts)",
          "D. ∏_acc_id (Transactions) ∩ ∏_acc_id (Accounts) = ∅"
        ],
        "correct_option": "B",
        "explanation": "Referential integrity requires foreign key values to be a subset of primary key values, making the set difference empty."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce database, Orders(OrderID, CustomerID) references Customers(CustomerID). Under referential integrity, what must the relational expression ∏_CustomerID(Orders) − ∏_CustomerID(Customers) evaluate to?",
        "options": [
          "A. Empty set (∅)",
          "B. The set of all CustomerIDs",
          "C. The set of customers who placed no orders",
          "D. The Cartesian product of both tables"
        ],
        "correct_option": "A",
        "explanation": "Referential integrity requires that every value of CustomerID in Orders must exist in Customers: ∏_CustomerID(Orders) ⊆ ∏_CustomerID(Customers). Therefore, subtracting Customers from Orders yields the empty set (∅)."
      }
    ]
  },
  {
    "id": "MCQ-049",
    "title": "Relational Algebra Theta Join Cardinality with Disjunctive Predicate",
    "topic": "Relational Algebra",
    "subtopic": "Theta Join & Disjunctive Conditions",
    "difficulty": "Hard",
    "source": "GATE CSE 2012 | Question: 50 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 14)",
    "source_file": "PYQs/CS_extracted/CS/2012_CS.pdf",
    "source_page": 14,
    "source_qnum": "Q.50",
    "evidence_snippet": "Q.50 Consider relations A, B and C: A(Id, Name, Age), B(Id, Name, Age), C(Id, Phone, Area). A has 3 tuples: (12, Arun, 60), (15, Shreya, 24), (99, Rohit, 11). B has 3 tuples: (15, Shreya, 24), (25, Hari, 40), (98, Rohit, 20), (99, Rohit, 11). C has 2 tuples: (10, 2200, 02), (99, 2100, 01). How many tuples does (A ∪ B) ⋈_{A.Id > 40 ∨ C.Id < 15} C contain? (A) 7",
    "prompt": "Consider relations A(Id, Name, Age), B(Id, Name, Age), and C(Id, Phone, Area):\n- A has tuples: (12, Arun, 60), (15, Shreya, 24), (99, Rohit, 11)\n- B has tuples: (15, Shreya, 24), (25, Hari, 40), (98, Rohit, 20), (99, Rohit, 11)\n- C has tuples: (10, 2200, 02), (99, 2100, 01)\nHow many tuples does the result of (A ∪ B) ⋈_{A.Id > 40 ∨ C.Id < 15} C contain?",
    "options": [
      "A. 7",
      "B. 4",
      "C. 5",
      "D. 9"
    ],
    "correct_option": "A",
    "explanation": "1. Compute relation union U = A ∪ B (set semantics):\nDistinct tuples in U: { (12, Arun, 60), (15, Shreya, 24), (25, Hari, 40), (98, Rohit, 20), (99, Rohit, 11) } -> 5 tuples with Ids {12, 15, 25, 98, 99}.\n2. Tuples in C: c1 = (10, 2200, 02), c2 = (99, 2100, 01).\n3. Evaluate theta join condition: A.Id > 40 ∨ C.Id < 15 for each pair (u, c) in U × C:\n- For c1 (C.Id = 10 < 15): Condition C.Id < 15 is TRUE for ALL 5 tuples in U -> 5 tuples generated.\n- For c2 (C.Id = 99 >= 15): Condition A.Id > 40 is TRUE for u with Id = 98 and Id = 99 (2 tuples) -> 2 tuples generated.\nTotal resulting tuples = 5 + 2 = 7 tuples.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EHR registry: Inpatient tables A and B union to 5 distinct patients with IDs {12, 15, 25, 98, 99}. They are joined with Clinic_Registry C containing {10, 99} on (A.Id > 40 OR C.Id < 15). What is the total tuple count?",
        "options": [
          "A. 4 tuples",
          "B. 6 tuples",
          "C. 7 tuples",
          "D. 10 tuples"
        ],
        "correct_option": "C",
        "explanation": "Clinic 10 matches all 5 patients (C.Id < 15); Clinic 99 matches the 2 patients with Id > 40. 5 + 2 = 7."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an automated banking data warehouse: Accounts(id, holder, balance) from two regional branches A and B are unioned (producing 5 distinct accounts with IDs 12, 15, 25, 98, 99). They are theta-joined with Channels(id, code) containing (10, 'WEB') and (99, 'ATM') on condition (A.id > 40 OR C.id < 15). How many tuples result?",
        "options": [
          "A. 5 tuples",
          "B. 7 tuples",
          "C. 4 tuples",
          "D. 9 tuples"
        ],
        "correct_option": "B",
        "explanation": "Channel (10, 'WEB') matches all 5 accounts (10 < 15); channel (99, 'ATM') matches the 2 accounts with ID > 40 (98, 99). 5 + 2 = 7."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Relation Discounts(Code, MinSpend) has 2 tuples: (D10, 100) and (D20, 500). Relation Carts(CartID, Value) has 5 carts with Values: 50, 150, 300, 600, 800. What is the number of tuples in Discounts ⨝_{Carts.Value >= Discounts.MinSpend} Carts?",
        "options": [
          "A. 6 tuples (D10 matches 4 carts >= 100; D20 matches 2 carts >= 500; total = 4 + 2 = 6)",
          "B. 10 tuples",
          "C. 2 tuples",
          "D. 5 tuples"
        ],
        "correct_option": "A",
        "explanation": "Cart values >= 100 are {150, 300, 600, 800} (4 tuples match D10). Cart values >= 500 are {600, 800} (2 tuples match D20). Total tuples = 4 + 2 = 6."
      }
    ]
  },
  {
    "id": "MCQ-050",
    "title": "SQL Subquery Evaluation with ALL Predicate on Empty Set",
    "topic": "SQL & Query Processing",
    "subtopic": "Quantified Comparison (ALL) with Empty Subqueries",
    "difficulty": "Medium",
    "source": "GATE CSE 2012 | Question: 51 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 14)",
    "source_file": "PYQs/CS_extracted/CS/2012_CS.pdf",
    "source_page": 14,
    "source_qnum": "Q.51",
    "evidence_snippet": "Q.51 Consider relations A(Id, Name, Age) and B(Id, Name, Age). A has 3 tuples: (12, Arun, 60), (15, Shreya, 24), (99, Rohit, 11). B has tuples for Shreya, Hari, Rohit. How many tuples does the following SQL query contain? SELECT A.Id FROM A WHERE A.Age > ALL (SELECT B.Age FROM B WHERE B.Name = 'Arun') (B) 3",
    "prompt": "Consider table A(Id, Name, Age) with 3 tuples: (12, 'Arun', 60), (15, 'Shreya', 24), (99, 'Rohit', 11), and table B(Id, Name, Age) containing tuples only for 'Shreya', 'Hari', and 'Rohit' (no row with Name = 'Arun'). How many tuples are returned by the query:\nSELECT A.Id FROM A WHERE A.Age > ALL (SELECT B.Age FROM B WHERE B.Name = 'Arun');",
    "options": [
      "A. 3",
      "B. 0",
      "C. 1",
      "D. 4"
    ],
    "correct_option": "A",
    "explanation": "1. The inner subquery `SELECT B.Age FROM B WHERE B.Name = 'Arun'` produces an EMPTY set because no row in B has Name = 'Arun'.\n2. In SQL predicate logic, `val > ALL (empty set)` evaluates to TRUE for any value (vacuous truth: there does not exist any element in the set for which `val > elem` is false).\n3. Consequently, the WHERE clause evaluates to TRUE for every single tuple in A.\nSince relation A contains 3 tuples, all 3 tuples are returned.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "An EHR clinical query checks Patient table A (3 patients) with `WHERE A.age > ALL (SELECT B.age FROM B WHERE B.condition = 'Smallpox')`. Since table B has 0 records for 'Smallpox', how many patient rows are returned?",
        "options": [
          "A. 0 rows",
          "B. 1 row",
          "C. 3 rows",
          "D. Error"
        ],
        "correct_option": "C",
        "explanation": "Comparing against an empty set with `> ALL` is vacuously true in SQL logic, returning all 3 rows of A."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a financial compliance audit table A(id, balance) with 3 records and table B(id, balance) containing no records for customer 'Apex': how many records are returned by `SELECT A.id FROM A WHERE A.balance > ALL (SELECT B.balance FROM B WHERE B.client = 'Apex')`?",
        "options": [
          "A. 0 records",
          "B. 3 records",
          "C. 1 record",
          "D. NULL"
        ],
        "correct_option": "B",
        "explanation": "When the inner query returns an empty result set, `> ALL` evaluates to vacuous TRUE for all rows of A."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce database with table Products(Price), what is the result of SELECT * FROM Products WHERE Price > ALL (SELECT Price FROM Products WHERE Category = 'NonExistentCategory')?",
        "options": [
          "A. All products in the table (because the subquery returns an empty set, and > ALL (empty set) evaluates to TRUE for every tuple)",
          "B. Zero products (empty result set)",
          "C. Only products with Price > 0",
          "D. A runtime SQL syntax error"
        ],
        "correct_option": "A",
        "explanation": "In three-valued SQL logic, a comparison v > ALL (S) is vacuously TRUE when the subquery set S is empty. Therefore, every row in Products satisfies the WHERE clause."
      }
    ]
  },
  {
    "id": "MCQ-051",
    "title": "Database Trigger Execution Semantics & Side Effects",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Definition and Event Execution",
    "difficulty": "Easy",
    "source": "ISRO CSE 2016 | Question: 58",
    "prompt": "Trigger is:",
    "options": [
      "A. Statement that enables to start any DBMS",
      "B. Statement that is executed by the user when debugging an application program",
      "C. The condition that the system tests for the validity of the database user",
      "D. Statement that is executed automatically by the system as a side effect of a modification of the database"
    ],
    "correct_option": "D",
    "explanation": "By formal definition in database systems, a trigger is a procedural statement or routine executed automatically by the DBMS engine as a side effect whenever a specified modification (INSERT, UPDATE, DELETE) is performed on a table or view.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical EMR, when a doctor updates a patient chart with an allergic reaction, how does the database automatically spawn an immediate alert notification to the pharmacy system?",
        "options": [
          "A. By firing a database trigger that executes automatically as a side effect of modifying the patient allergies relation",
          "B. By requiring the doctor to manually run a Python debugging script",
          "C. By relying on an unindexed night cron job",
          "D. By verifying the network card speed"
        ],
        "correct_option": "A",
        "explanation": "A trigger automatically executes notification code as a side effect of the clinical record update."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In core banking, how does an engine record every unauthorized wire attempt into an immutable audit table without requiring application code changes?",
        "options": [
          "A. By using an automated database trigger executed by the system as a side effect of suspicious transaction updates",
          "B. By deleting the customer profile",
          "C. By setting account balances to zero",
          "D. By converting the database into a CSV file"
        ],
        "correct_option": "A",
        "explanation": "Triggers execute audit logging automatically as side effects of data modifications."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When an online order is placed, how does the database automatically decrement warehouse inventory and log a shipment dispatch task?",
        "options": [
          "A. Through an automated trigger executed by the DBMS engine as a side effect of order creation",
          "B. By rebooting the database server",
          "C. By dropping the products table index",
          "D. By asking the customer to confirm warehouse location"
        ],
        "correct_option": "A",
        "explanation": "Triggers execute side-effect logic (inventory decrement) upon order insertion."
      }
    ]
  },
  {
    "id": "MCQ-052",
    "title": "Relational Object Access Control: GRANT & REVOKE",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Data Control Language (DCL) Privileges",
    "difficulty": "Easy",
    "source": "ISRO CSE 2007 | Question: 47",
    "prompt": "Which SQL commands are used to control access privileges over objects in a relational database?",
    "options": [
      "A. CASCADE & MVD",
      "B. GRANT & REVOKE",
      "C. QUE & QUIST",
      "D. COMMIT & ROLLBACK"
    ],
    "correct_option": "B",
    "explanation": "GRANT and REVOKE are the standard Data Control Language (DCL) commands in SQL. GRANT bestows specific access privileges (SELECT, INSERT, UPDATE, DELETE) on database objects to users/roles, while REVOKE withdraws previously granted permissions.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Which SQL DCL statements allow a Hospital DBA to assign medical chart viewing rights to attending physicians and strip those rights when a physician rotates out?",
        "options": [
          "A. SELECT & INSERT",
          "B. CREATE & DROP",
          "C. GRANT & REVOKE",
          "D. SAVEPOINT & ROLLBACK"
        ],
        "correct_option": "C",
        "explanation": "GRANT assigns chart permissions; REVOKE withdraws access rights."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In financial compliance, what SQL commands manage employee access rights to sensitive credit ledger tables?",
        "options": [
          "A. ALTER & TRUNCATE",
          "B. CHECK & ASSERTION",
          "C. ENCRYPT & DECRYPT",
          "D. GRANT & REVOKE"
        ],
        "correct_option": "D",
        "explanation": "GRANT and REVOKE govern authorization and role privileges in relational engines."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "How does a marketplace administrator give vendor roles the ability to update product prices while removing their access to buyer payment details?",
        "options": [
          "A. Using LOCK and UNLOCK",
          "B. Using GRANT to authorize price updates and REVOKE to restrict payment records",
          "C. Using COMMIT and ROLLBACK",
          "D. Using MERGE and UPSERT"
        ],
        "correct_option": "B",
        "explanation": "DCL access control commands GRANT and REVOKE manage object-level privileges."
      }
    ]
  },
  {
    "id": "MCQ-053",
    "title": "SQL Aggregate Functions and NULL Values",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Aggregate Handling of NULL Tuples",
    "difficulty": "Easy",
    "source": "ISRO CSE 2007 | Question: 48",
    "prompt": "Which of the following is a standard aggregate function in SQL, and how does it handle NULL values?",
    "options": [
      "A. SELECT; it returns NULL",
      "B. AVG; it ignores NULL values when computing the mean across tuples",
      "C. DISTINCT; it converts NULL to zero",
      "D. ORDER BY; it places NULLs at the beginning only"
    ],
    "correct_option": "B",
    "explanation": "AVG is a standard SQL aggregate function. In relational SQL standards, aggregate functions (SUM, AVG, MIN, MAX) automatically ignore (filter out) NULL values from computation, except COUNT(*), which counts all matching rows regardless of nullness.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When calculating the average dosage administered to ICU patients, how does the SQL AVG(dosage) function handle records where dosage is NULL?",
        "options": [
          "A. It aborts the query with an exception",
          "B. It treats NULL as 0 mg, depressing the average",
          "C. It ignores the NULL rows and averages only non-null dosage values",
          "D. It replaces NULL with the maximum dose"
        ],
        "correct_option": "C",
        "explanation": "SQL AVG ignores NULLs, calculating the true mean of recorded dosages."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In computing AVG(overdraft_fee) on checking accounts where accounts without fees store NULL, how does the query engine evaluate the result?",
        "options": [
          "A. It ignores the NULL accounts, computing the mean fee across fee-paying accounts only",
          "B. It fails to compile",
          "C. It converts the entire ledger to zero",
          "D. It treats NULL as $100 penalty"
        ],
        "correct_option": "A",
        "explanation": "Aggregate functions ignore NULL tuples during calculation."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When computing AVG(discount_amount) on cart items where non-discounted products store NULL, what does SQL return?",
        "options": [
          "A. 0.00 always",
          "B. The average discount of only the discounted items (NULLs ignored)",
          "C. An infinite loop",
          "D. A table scan error"
        ],
        "correct_option": "B",
        "explanation": "AVG ignores NULLs, reflecting average discount among items having discounts."
      }
    ]
  },
  {
    "id": "MCQ-054",
    "title": "Purpose of Foreign Key in Referential Integrity",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Foreign Key Invariants and Parent Tables",
    "difficulty": "Easy",
    "source": "ISRO CSE 2009 | Question: 72",
    "prompt": "The fundamental purpose of defining a 'Foreign Key' constraint in a relational database table is to ensure:",
    "options": [
      "A. Null integrity",
      "B. Referential integrity between related tables",
      "C. Domain integrity only",
      "D. Faster physical sorting on disk"
    ],
    "correct_option": "B",
    "explanation": "A foreign key establishes a relationship between a child table attribute and a candidate/primary key of a parent table, ensuring referential integrity—preventing orphan records that reference non-existent parent rows.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why does table Patient_Vitals include a foreign key referencing Patients(Patient_ID)?",
        "options": [
          "A. To ensure every recorded vital measurement references an existing, valid patient (referential integrity)",
          "B. To automatically encrypt patient names",
          "C. To speed up network backups",
          "D. To delete all vital logs daily"
        ],
        "correct_option": "A",
        "explanation": "Foreign keys enforce referential integrity between vitals and patient master records."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why must Account_Transactions contain a foreign key referencing Accounts(Account_Number)?",
        "options": [
          "A. To preserve referential integrity, guaranteeing transactions cannot exist for bogus accounts",
          "B. To double the bank's interest rates",
          "C. To replace the primary key index",
          "D. To prevent account numbers from having letters"
        ],
        "correct_option": "A",
        "explanation": "Foreign keys preserve referential integrity across ledger tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "What integrity guarantee does a foreign key provide between Order_Lines and Products?",
        "options": [
          "A. Immediate delivery of ordered items",
          "B. Referential integrity, ensuring no customer can order a product that does not exist in the catalog",
          "C. Free shipping on all carts",
          "D. Elimination of SQL joins"
        ],
        "correct_option": "B",
        "explanation": "Foreign keys guarantee referential integrity against orphan order items."
      }
    ]
  },
  {
    "id": "MCQ-055",
    "title": "Natural Join Equivalence and Tuple Multiplication",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Relational Natural Join Cardinality",
    "difficulty": "Medium",
    "source": "ISRO CSE 2017 | Question: 7",
    "prompt": "Given relation Overtime_allowance(Employee, Department, OT_allowance). What is the output cardinality of: 'SELECT COUNT(*) FROM ((SELECT Employee, Department FROM Overtime_allowance) NATURAL JOIN (SELECT Department, OT_allowance FROM Overtime_allowance) AS T)' when multiple employees share the same department?",
    "options": [
      "A. It is always equal to the original number of rows in Overtime_allowance",
      "B. It can exceed the original count because tuples within the same department join in a Cartesian product across that department",
      "C. It always returns 0",
      "D. It produces a syntax error due to alias scoping"
    ],
    "correct_option": "B",
    "explanation": "Natural join equates common attribute Department. If a department has k employees and m distinct OT allowances, projecting Department with Employee and joining with Department with OT produces k * m rows for that department, potentially multiplying tuples.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In Nurse_Shifts(Nurse_ID, Ward, Shift_Type), decomposing by (Nurse,Ward) and (Ward,Shift) and natural-joining on Ward yields:",
        "options": [
          "A. More records than the original if multiple nurses and shift types exist in the same ward (lossy decomposition)",
          "B. A compiler error",
          "C. Exactly 0 records",
          "D. Instant deletion of nurse records"
        ],
        "correct_option": "A",
        "explanation": "Natural joining on non-candidate key Ward produces cross-product combinations per ward."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In Loan_Risk(Officer_ID, Branch, Risk_Category), joining projections on Branch results in tuple multiplication when:",
        "options": [
          "A. Multiple loan officers and multiple risk categories co-exist in the same branch",
          "B. Branch names are strings",
          "C. Interest rates are zero",
          "D. Officers have zero loans"
        ],
        "correct_option": "A",
        "explanation": "Tuple multiplication occurs when joining on non-key duplicate attributes."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In Supplier_Inventory(Supplier_ID, Warehouse, Item_Type), joining on Warehouse creates duplicate tuples because:",
        "options": [
          "A. Warehouses are physical buildings",
          "B. Each supplier in a warehouse joins with all item types stored in that warehouse",
          "C. Items have unique SKUs",
          "D. Suppliers are external entities"
        ],
        "correct_option": "B",
        "explanation": "Common join attribute Warehouse generates pairwise combinations among associated rows."
      }
    ]
  },
  {
    "id": "MCQ-056",
    "title": "Distinct Projection and Multiset Elimination",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "SELECT DISTINCT Cardinality Invariants",
    "difficulty": "Medium",
    "source": "ISRO CSE 2018 | Question: 40",
    "prompt": "Given relations R(w, x) and S(y, z), the result of query 'SELECT DISTINCT w, x FROM R, S' is GUARANTEED to be identical to relation R if and only if:",
    "options": [
      "A. Relation S is completely empty",
      "B. Relation S contains at least one tuple, and R contains no duplicate tuples",
      "C. Relations R and S have identical schemas",
      "D. S has strictly more rows than R"
    ],
    "correct_option": "B",
    "explanation": "If S has zero tuples, the Cartesian product R × S is empty. If S has at least one tuple, projecting R.w, R.x extracts rows of R. The DISTINCT operator then removes duplicates from R. Thus, the result equals R iff S is non-empty and R has no duplicate rows.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinic tables Patients(ID, Name) and Clinics(Clinic_Code, City), when does 'SELECT DISTINCT ID, Name FROM Patients, Clinics' exactly equal Patients?",
        "options": [
          "A. When Clinics has at least 1 record and Patients has no duplicate tuples",
          "B. When all patients live in the clinic city",
          "C. When Clinics is empty",
          "D. When Doctors approve the query"
        ],
        "correct_option": "A",
        "explanation": "A non-empty Clinics table permits projection; lack of duplicates in Patients ensures DISTINCT equals R."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In Accounts(Acc_ID, Balance) and Branches(Branch_ID, City), 'SELECT DISTINCT Acc_ID, Balance FROM Accounts, Branches' equals Accounts when:",
        "options": [
          "A. Branches is non-empty and Accounts contains unique tuples",
          "B. Balance is always positive",
          "C. Every account has an assigned branch",
          "D. Branches is empty"
        ],
        "correct_option": "A",
        "explanation": "Non-empty second table ensures non-empty product; distinct accounts ensures set equality."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In Products(SKU, Price) and Hubs(Hub_ID, Region), 'SELECT DISTINCT SKU, Price FROM Products, Hubs' equals Products when:",
        "options": [
          "A. Hubs has zero records",
          "B. Hubs has at least one record and Products has unique primary keys",
          "C. Shipping is free",
          "D. Prices are integers"
        ],
        "correct_option": "B",
        "explanation": "Product projection matches base table when Hubs is non-empty and Products has no duplicates."
      }
    ]
  },
  {
    "id": "MCQ-057",
    "title": "Correlated Relational Division Querying",
    "topic": "Relational Calculus & Relational Algebra",
    "subtopic": "Correlated NOT EXISTS Division Patterns",
    "difficulty": "Hard",
    "source": "ISRO CSE 2018 | Question: 42",
    "prompt": "Given relations Students(Roll, Name), Courses(Course_No, Course_Name), Grades(Roll, Course_No, Grade). Which SQL query retrieves the names of all students who have enrolled in EVERY course?",
    "options": [
      "A. SELECT Name FROM Students S WHERE NOT EXISTS (SELECT Course_No FROM Courses C WHERE NOT EXISTS (SELECT * FROM Grades G WHERE G.Roll = S.Roll AND G.Course_No = C.Course_No))",
      "B. SELECT Name FROM Students NATURAL JOIN Grades NATURAL JOIN Courses",
      "C. SELECT Name FROM Students S WHERE (SELECT COUNT(*) FROM Grades G WHERE G.Roll = S.Roll) = 0",
      "D. SELECT Name FROM Students S WHERE S.Roll IN (SELECT Roll FROM Courses)"
    ],
    "correct_option": "A",
    "explanation": "This is the standard SQL idiom for relational division using double NOT EXISTS: find students S such that there does NOT exist a course C for which there does NOT exist a grade record pairing student S with course C.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "To identify physicians who have completed EVERY mandatory hospital training module, the clinical query uses double negation:",
        "options": [
          "A. SELECT Doc_Name FROM Doctors D WHERE Doc_ID = 1",
          "B. SELECT Doc_Name FROM Doctors D WHERE NOT EXISTS (SELECT Mod_ID FROM Training T WHERE NOT EXISTS (SELECT * FROM Doc_Training DT WHERE DT.Doc_ID = D.Doc_ID AND DT.Mod_ID = T.Mod_ID))",
          "C. SELECT Doc_Name FROM Doctors WHERE Training IS NULL",
          "D. SELECT * FROM Doctors CROSS JOIN Training"
        ],
        "correct_option": "B",
        "explanation": "Double NOT EXISTS implements relational division for mandatory training compliance."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "To find investment portfolios that hold EVERY stock in the S&P 500 index, the compliance system runs:",
        "options": [
          "A. Single join on stock ticker",
          "B. Simple sum of stock quantities",
          "C. Double NOT EXISTS verifying there is no S&P stock missing from the portfolio's holdings",
          "D. Group by with count = 0"
        ],
        "correct_option": "C",
        "explanation": "Relational division verifies comprehensive index coverage."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To find customers who have purchased EVERY product launched in the 2026 flagship line:",
        "options": [
          "A. SELECT Customer_ID FROM Customers WHERE Status = 'VIP'",
          "B. Truncate orders table",
          "C. Outer join on Customer_ID",
          "D. Query with correlated double NOT EXISTS finding customers with no missing flagship product purchases"
        ],
        "correct_option": "D",
        "explanation": "Double negation guarantees universal quantification across the product set."
      }
    ]
  },
  {
    "id": "MCQ-058",
    "title": "ACID Properties: Fundamental Transaction Invariants",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "ACID Properties and Invariant Semantics",
    "difficulty": "Easy",
    "source": "ISRO CSE 2017 | Question: 6",
    "prompt": "The ACID properties of database transactions stand for:",
    "options": [
      "A. Atomicity, consistency, isolation, database",
      "B. Atomicity, consistency, isolation, durability",
      "C. Atomicity, consistency, integrity, durability",
      "D. Authentication, consistency, isolation, durability"
    ],
    "correct_option": "B",
    "explanation": "ACID stands for: Atomicity (all-or-nothing execution), Consistency (preserves database integrity constraints), Isolation (concurrent execution equivalent to serial), and Durability (committed updates survive system crashes).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical EMR databases, what do ACID guarantees ensure for electronic patient prescriptions?",
        "options": [
          "A. Atomicity (all meds recorded or none), Consistency (valid dosage rules), Isolation (no chart overwrites), Durability (persisted past power loss)",
          "B. Access control, cryptography, integrity, databases",
          "C. Automated Clinical Insurance Dispatches",
          "D. Audio recording of doctor orders"
        ],
        "correct_option": "A",
        "explanation": "ACID guarantees transactional integrity in healthcare systems."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "For core banking wire transfers, ACID properties guarantee:",
        "options": [
          "A. Transfers never lose money (Atomicity), balance rules hold (Consistency), concurrent wires don't interfere (Isolation), commits survive crashes (Durability)",
          "B. Only debit cards can be used",
          "C. All currency is converted to gold",
          "D. Accounts can never be closed"
        ],
        "correct_option": "A",
        "explanation": "ACID properties underpin ledger correctness and financial audit compliance."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce cart transactions, ACID properties protect against:",
        "options": [
          "A. Customer returns",
          "B. Partial orders charging cards without saving items (Atomicity) and overselling items (Isolation)",
          "C. High delivery fees",
          "D. Slow internet connections"
        ],
        "correct_option": "B",
        "explanation": "ACID prevents orphaned payments and inventory race conditions."
      }
    ]
  },
  {
    "id": "MCQ-059",
    "title": "Timestamp Ordering Protocol & Rollback Invariants",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Timestamp Ordering and Thomas Write Rule",
    "difficulty": "Medium",
    "source": "ISRO CSE 2018 | Question: 55",
    "prompt": "In the basic Timestamp Ordering (TO) concurrency control protocol, if transaction Ti attempts to execute read(X) when timestamp TS(Ti) < W_timestamp(X):",
    "options": [
      "A. Ti is allowed to read X immediately",
      "B. Ti is rolled back and restarted with a new timestamp because it attempted to read an overwritten value",
      "C. The write on X is reversed",
      "D. The system halts"
    ],
    "correct_option": "B",
    "explanation": "In basic TO: If TS(Ti) < W_timestamp(X), transaction Ti needed to read an older value of X that has already been overwritten by a younger transaction. Therefore, Ti is too late: Ti is rolled back, aborted, and restarted with a new timestamp.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A physician chart audit transaction T1 (ts 10:00) tries to read vitals overwritten by nurse T2 (ts 10:05). Under Timestamp Ordering:",
        "options": [
          "A. T1 is aborted and restarted with a new timestamp to prevent reading an overwritten clinical state",
          "B. Patient is discharged",
          "C. T1 overwrites T2",
          "D. Hospital servers shut down"
        ],
        "correct_option": "A",
        "explanation": "Timestamp protocol aborts outdated reads that arrive after newer writes."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In ledger processing, wire transfer T1 (ts=100) attempts to read an account balance whose W_timestamp is 150. What occurs?",
        "options": [
          "A. T1 is aborted and rolled back because its read is obsolete",
          "B. Balance is reset to zero",
          "C. Transfer commits anyway",
          "D. T1 receives free funds"
        ],
        "correct_option": "A",
        "explanation": "Arriving after a newer write violates timestamp order, requiring T1 rollback."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "A pricing batch job T1 (ts=10) reads product inventory whose W_timestamp is 15. Under Basic Timestamp Ordering:",
        "options": [
          "A. Inventory is locked permanently",
          "B. T1 is rolled back and restarted with a fresh timestamp",
          "C. All customer carts are cleared",
          "D. Price becomes zero"
        ],
        "correct_option": "B",
        "explanation": "Outdated read requests trigger rollback under timestamp ordering protocols."
      }
    ]
  },
  {
    "id": "MCQ-060",
    "title": "Raymond Tree-Based Distributed Mutual Exclusion",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Distributed Mutual Exclusion Algorithms",
    "difficulty": "Hard",
    "source": "ISRO CSE 2020 | Question: 22",
    "prompt": "Raymond's tree-based algorithm for distributed mutual exclusion organizes network nodes into a directed logical tree. What is its key operational property?",
    "options": [
      "A. It ensures no deadlock, but starvation may occur in rare unweighted topologies",
      "B. Messages are broadcast to all nodes simultaneously",
      "C. It requires O(N) message exchanges per critical section entry",
      "D. It uses physical synchronized clocks instead of logical tokens"
    ],
    "correct_option": "A",
    "explanation": "Raymond's algorithm routes requests along directed edges of a spanning tree toward the token holder. It is deadlock-free and achieves O(log N) average message complexity, though unweighted FIFO queueing can lead to starvation under pathological configurations.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a distributed multi-hospital surgical scheduling network using Raymond's tree algorithm to reserve specialized MRI suites:",
        "options": [
          "A. All hospitals broadcast to every other hospital every second",
          "B. Requests travel along the tree toward the token holder without deadlock, requiring only O(log N) messages on average",
          "C. Deadlocks occur frequently in MRI allocation",
          "D. MRI machines can only be reserved by one hospital per month"
        ],
        "correct_option": "B",
        "explanation": "Raymond's algorithm delivers deadlock-free token passing with logarithmic message complexity."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a geographically distributed banking consortium locking shared currency reserves via Raymond's tree:",
        "options": [
          "A. Every bank must send messages to all 500 consortium members",
          "B. High latency causes ledger loops",
          "C. Logical tree routing guarantees deadlock freedom with O(log N) message overhead",
          "D. Network switches must be replaced daily"
        ],
        "correct_option": "C",
        "explanation": "Tree-structured request forwarding avoids deadlocks in distributed coordination."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a global multi-region inventory lock coordinator using Raymond's tree algorithm:",
        "options": [
          "A. Orders fail if region count exceeds 10",
          "B. Broadcast storms flood the backbone",
          "C. Databases run without consensus",
          "D. Distributed inventory locks are acquired along tree edges without deadlocks in O(log N) steps"
        ],
        "correct_option": "D",
        "explanation": "Raymond's algorithm provides scalable, deadlock-free token arbitration across regions."
      }
    ]
  },
  {
    "id": "MCQ-061",
    "title": "8085 Interrupt Triggering: Level vs Edge Sensitivity",
    "topic": "Computer Architecture: Interrupts & Execution",
    "subtopic": "Microprocessor Interrupt Triggering Modes",
    "difficulty": "Medium",
    "source": "ISRO CSE 2008 | Question: 45",
    "prompt": "In the 8085 microprocessor architecture, how is the TRAP non-maskable interrupt triggered?",
    "options": [
      "A. It is level-triggered only",
      "B. It is negative edge-triggered only",
      "C. It is both level and positive edge-sensitive (edge-and-level triggered) to prevent false triggering by noise",
      "D. It is software-triggered via the RST 0 instruction only"
    ],
    "correct_option": "C",
    "explanation": "In 8085 architecture, TRAP (the highest priority non-maskable interrupt) is both edge- and level-sensitive. The edge sensitivity prevents false triggering on noise, while level sensitivity ensures the line remains active until the CPU samples it during opcode fetch.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an ICU life-support monitor connected to an 8085 embedded controller, why is the emergency cardiac arrest interrupt configured as edge-and-level sensitive?",
        "options": [
          "A. To ensure a single noise spike does not trigger a false alert, while guaranteeing prolonged sensor signals are recognized",
          "B. To delay cardiac arrest processing by 10 minutes",
          "C. To turn off hospital lights",
          "D. Because medical microprocessors cannot detect levels"
        ],
        "correct_option": "A",
        "explanation": "Dual edge-and-level sensitivity eliminates spurious noise while ensuring persistent alarms are processed."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an ATM hardware controller, why is the tamper-detection sensor wired to an edge-and-level sensitive interrupt line?",
        "options": [
          "A. To format the ATM hard drive",
          "B. To filter transient electrical noise while ensuring active physical breaches keep the interrupt asserted",
          "C. To speed up cash dispensing",
          "D. To print receipts faster"
        ],
        "correct_option": "B",
        "explanation": "Edge-and-level triggering prevents nuisance trips while ensuring genuine tamper signals are handled."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an automated warehouse conveyor robot, why does the emergency stop sensor use edge-and-level triggering?",
        "options": [
          "A. It prevents mechanical vibration from causing false halts while guaranteeing sustained stop signals freeze the motor",
          "B. To disable barcode scanning",
          "C. To increase package throughput",
          "D. To reboot the Wi-Fi router"
        ],
        "correct_option": "A",
        "explanation": "Dual triggering filters sensor bounce while honoring persistent safety stops."
      }
    ]
  },
  {
    "id": "MCQ-062",
    "title": "Hardware Edge Triggering in Sequential Flip-Flops",
    "topic": "Digital Logic: Flip-Flops & Hardware Triggers",
    "subtopic": "Clock Edge Triggering vs Level Latching",
    "difficulty": "Easy",
    "source": "ISRO CSE 2007 | Question: 31",
    "prompt": "In digital sequential circuits, what is the primary operational advantage of an edge-triggered flip-flop over a level-sensitive latch?",
    "options": [
      "A. Edge-triggered circuits eliminate race-around conditions by sampling inputs only during clock transitions",
      "B. Latches consume zero dynamic power",
      "C. Edge-triggered flip-flops require no clock input",
      "D. Latches operate at higher gigahertz frequencies"
    ],
    "correct_option": "A",
    "explanation": "Level-sensitive latches remain transparent as long as the clock level is high, causing race-around conditions if inputs change during the active pulse. Edge-triggered flip-flops sample input strictly during the rising or falling clock edge, preventing race conditions.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a digital biomedical pacemaker circuit, why are register stages designed with edge-triggered flip-flops rather than simple latches?",
        "options": [
          "A. To allow doctors to manually adjust clock frequencies with a knob",
          "B. To eliminate race-around condition errors during clock transitions, ensuring precise heartbeat pulse timing",
          "C. Because pacemakers run without batteries",
          "D. To decrease medical memory capacity"
        ],
        "correct_option": "B",
        "explanation": "Edge triggering prevents state race-around, ensuring rock-solid pacemaker timing."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a hardware security module (HSM) hashing cryptographic signatures, why are pipeline stages edge-triggered?",
        "options": [
          "A. To allow unencrypted PIN transmission",
          "B. To eliminate internal logic gates",
          "C. To isolate clock domains and eliminate race-around conditions across hashing stages",
          "D. To reduce clock speed to 1 Hz"
        ],
        "correct_option": "C",
        "explanation": "Edge-triggered registers prevent race conditions across cryptographic pipeline stages."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In automated barcode sorter optical decoding logic, why are shift registers edge-triggered?",
        "options": [
          "A. To slow down package sorting",
          "B. To bypass parity check bits",
          "C. To allow manual package routing",
          "D. To sample sensor photodiode outputs strictly on the clock edge, preventing race-around blur"
        ],
        "correct_option": "D",
        "explanation": "Edge triggering guarantees clean single-sample shifts without level-sensitive race anomalies."
      }
    ]
  },
  {
    "id": "MCQ-063",
    "title": "Network Medium Access Control (MAC) Sublayer Protocol",
    "topic": "Computer Networks: Access Control & Security",
    "subtopic": "Medium Access Control and CSMA/CD",
    "difficulty": "Medium",
    "source": "ISRO CSE 2008 | Question: 4",
    "prompt": "In the IEEE 802.3 Ethernet protocol, what is the core role of the Medium Access Control (MAC) sublayer in the Data Link Layer?",
    "options": [
      "A. Resolving contention and regulating transmission access over a shared physical channel using CSMA/CD",
      "B. Routing IP packets across autonomous systems via BGP",
      "C. Establishing end-to-end TCP byte streams",
      "D. Performing domain name translation"
    ],
    "correct_option": "A",
    "explanation": "The Medium Access Control (MAC) sublayer manages access to shared physical media, performs frame delimiting, error checking (CRC), and resolves transmission collisions using protocols like CSMA/CD or CSMA/CA.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital telemetry Wi-Fi network carrying real-time vital streams, what is the role of the MAC layer access control protocol?",
        "options": [
          "A. Diagnosing patient illnesses",
          "B. Regulating airwave access among multiple patient transmitters to prevent overlapping transmission collisions",
          "C. Converting analog EKG to PDF",
          "D. Printing hospital invoices"
        ],
        "correct_option": "B",
        "explanation": "MAC protocols coordinate airwave sharing among telemetry devices to avoid collisions."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a high-frequency trading LAN, what does the MAC sublayer arbitrate across trading server network cards?",
        "options": [
          "A. Stock market opening hours",
          "B. Currency exchange rates",
          "C. Access to the physical Ethernet cable to transmit market order frames without collision",
          "D. Bank vault locks"
        ],
        "correct_option": "C",
        "explanation": "MAC sublayer controls frame access to the shared physical network medium."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an automated warehouse autonomous guided vehicle (AGV) network, what is the purpose of MAC access control?",
        "options": [
          "A. Calculating product prices",
          "B. Packing cardboard boxes",
          "C. Managing customer credit card accounts",
          "D. Preventing packet collisions when multiple warehouse robots transmit telemetry on the shared RF channel"
        ],
        "correct_option": "D",
        "explanation": "MAC protocols arbitrate shared radio medium access across robot transmitters."
      }
    ]
  },
  {
    "id": "MCQ-064",
    "title": "Operating System Discretionary Access Control (DAC)",
    "topic": "Operating Systems: Security & Access Control",
    "subtopic": "DAC Models and Permission Matrices",
    "difficulty": "Medium",
    "source": "ISRO CSE 2014 | Question: 39",
    "prompt": "In Operating System security models, what defines Discretionary Access Control (DAC)?",
    "options": [
      "A. Access rights are determined strictly by system-wide mandatory security labels (e.g. Top Secret)",
      "B. The owner of an object has full discretion to grant or revoke access privileges (e.g. read/write/execute) to other users",
      "C. Access is granted based solely on the time of day",
      "D. All users possess identical root permissions"
    ],
    "correct_option": "B",
    "explanation": "In Discretionary Access Control (DAC), access permissions are based on the identity of subjects and authorizations. The owner/creator of a file or database object has the discretion to grant or revoke access rights to other subjects.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Under DAC in a medical research OS, if Dr. Smith creates a genomic clinical trial dataset, what authority does Dr. Smith hold?",
        "options": [
          "A. Dr. Smith has discretion to grant read/write permissions on that dataset to collaborating researchers",
          "B. All hospital staff automatically gain root access",
          "C. The hospital CEO must approve every single file read",
          "D. Dr. Smith cannot access his own data"
        ],
        "correct_option": "A",
        "explanation": "In DAC, the dataset owner controls discretionary sharing of permissions with peers."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a banking financial modeling system using DAC, what power does a financial analyst have over an authored spreadsheet?",
        "options": [
          "A. The analyst can grant read access to auditors while withholding write access",
          "B. The analyst overrides system firewall rules",
          "C. DAC prevents anyone from opening the spreadsheet",
          "D. The analyst can alter the core banking ledger"
        ],
        "correct_option": "A",
        "explanation": "DAC allows object creators to selectively share permissions with auditors."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a vendor portal running on DAC, what control does a merchant have over uploaded catalog image files?",
        "options": [
          "A. Complete control over customer payment gateways",
          "B. Discretion to grant read permissions to public buyers while revoking edit permissions from competing vendors",
          "C. The ability to modify web server source code",
          "D. No control; all files are public domain"
        ],
        "correct_option": "B",
        "explanation": "DAC empowers file owners to govern read/write access privileges."
      }
    ]
  },
  {
    "id": "MCQ-065",
    "title": "Kernel vs User Privilege Rings & Protection Domains",
    "topic": "Operating Systems: Security & Access Control",
    "subtopic": "Privilege Levels and System Call Traps",
    "difficulty": "Medium",
    "source": "ISRO CSE 2017 | Question: 70",
    "prompt": "Why do modern CPUs and operating systems enforce dual-mode operation (User Mode vs Kernel/Supervisor Mode)?",
    "options": [
      "A. To allow user applications to directly modify memory management page tables",
      "B. To protect operating system memory and hardware devices from unauthorized access or accidental corruption by user processes",
      "C. To eliminate the need for device drivers",
      "D. To double CPU clock frequency in user mode"
    ],
    "correct_option": "B",
    "explanation": "Dual-mode operation provides hardware-enforced protection. Privileged instructions (I/O instructions, CPU halt, MMU page table modifications) can only execute in Kernel Mode (Ring 0), safeguarding the system from rogue or buggy user processes.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In hospital ICU patient monitoring computers, why are bedside nurse applications executed in User Mode rather than Kernel Mode?",
        "options": [
          "A. To ensure a bug in the bedside UI application cannot corrupt kernel memory or crash the life-support operating system",
          "B. To prevent monitoring devices from using electricity",
          "C. Because nurses are not software engineers",
          "D. To allow patient applications to directly access the CPU bus"
        ],
        "correct_option": "A",
        "explanation": "User mode isolates application crashes from the critical OS kernel."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why must algorithmic trading algorithms run in User Mode while the network socket driver runs in Kernel Mode?",
        "options": [
          "A. To prevent rogue trading software from overwriting kernel page tables or bypassing network security filters",
          "B. Because trading algorithms only use floating-point numbers",
          "C. To make the trading engine single-threaded",
          "D. To slow down competitor algorithms"
        ],
        "correct_option": "A",
        "explanation": "Kernel protection rings prevent user programs from compromising system integrity."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In cloud servers hosting e-commerce storefronts, what is the role of privilege rings?",
        "options": [
          "A. Speeding up HTTP web page downloads",
          "B. Restricting tenant web processes to Ring 3 (User) so they cannot compromise the hypervisor or host OS in Ring 0",
          "C. Eliminating the need for SSL certificates",
          "D. Automatically refunding canceled orders"
        ],
        "correct_option": "B",
        "explanation": "Dual mode protects cloud operating systems from unauthorized access by tenant web processes."
      }
    ]
  },
  {
    "id": "MCQ-066",
    "title": "Two-Phase Commit Protocol in Distributed DBMS",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Distributed Transactions and 2PC Protocol",
    "difficulty": "Hard",
    "source": "ISRO CSE 2023 | Question: 49",
    "prompt": "In the Two-Phase Commit (2PC) protocol across distributed database nodes, what occurs if any single cohort participant votes 'NO' during Phase 1 (Prepare Phase)?",
    "options": [
      "A. The coordinator ignores the vote and commits anyway",
      "B. The coordinator broadcasts a global 'ABORT' message to all participants, ensuring atomicity is preserved",
      "C. The cohort voting NO is permanently disconnected from the cluster",
      "D. Phase 2 is skipped and data remains in a half-committed state"
    ],
    "correct_option": "B",
    "explanation": "In 2PC, unanimous consent is required to commit. If even one cohort node votes NO (or times out) during Phase 1 (Prepare), the coordinator broadcasts a GLOBAL ABORT to all nodes during Phase 2, rolling back all local sub-transactions to guarantee global Atomicity.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a distributed hospital database spanning Pharmacy, Billing, and Surgery, what happens if Pharmacy votes NO during a drug-order 2PC prepare phase?",
        "options": [
          "A. The transaction coordinator issues a global ABORT to all wards, rolling back the surgery and billing records",
          "B. Billing charges the patient double",
          "C. Surgery proceeds without medication",
          "D. The pharmacy server is deleted"
        ],
        "correct_option": "A",
        "explanation": "Unanimous 2PC agreement is required; one NO vote aborts the distributed transaction everywhere."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "During a cross-border wire transfer between Bank A (US) and Bank B (Europe), Bank B's ledger server votes NO due to compliance holds. What does 2PC dictate?",
        "options": [
          "A. Coordinator issues Global ABORT; Bank A cancels the debit and Bank B cancels the pending credit",
          "B. Bank B is fined by the coordinator",
          "C. The wire is placed in an infinite loop",
          "D. Bank A sends the money regardless"
        ],
        "correct_option": "A",
        "explanation": "A single negative vote triggers global abort, preventing money from vanishing into limbo."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "During checkout spanning Inventory DB, Payment Gateway DB, and Shipping DB, Payment votes NO. How does 2PC resolve this?",
        "options": [
          "A. Inventory is permanently decremented anyway",
          "B. Coordinator broadcasts Global ABORT; Inventory unreserves the stock and Shipping cancels the label",
          "C. Customer is banned from website",
          "D. Shipping ships an empty package"
        ],
        "correct_option": "B",
        "explanation": "Global abort ensures inventory and shipping roll back if payment authorization fails."
      }
    ]
  },
  {
    "id": "MCQ-067",
    "title": "Checkpoint Recovery and Log Redo Pass",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Checkpoint Recovery and Redo Pass",
    "difficulty": "Hard",
    "source": "ISRO CSE 2013 | Question: 23",
    "prompt": "In database log-based recovery, what is the primary benefit of writing periodic 'CHECKPOINT' records to the log?",
    "options": [
      "A. It permanently prevents any future system crashes",
      "B. It bounds recovery time by guaranteeing that all log records prior to the checkpoint have already flushed their dirty buffer pages to disk",
      "C. It converts the database to read-only mode",
      "D. It eliminates the need for transaction undo operations"
    ],
    "correct_option": "B",
    "explanation": "Checkpoints ensure that modified dirty database buffer pool pages are written to persistent storage. During crash recovery, the recovery manager does not need to scan the log from the beginning of time; it only needs to scan back to the latest active checkpoint.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why does a hospital clinical database execute checkpoints every 15 minutes?",
        "options": [
          "A. To ensure dirty patient chart updates are flushed to disk, limiting reboot recovery time after power loss",
          "B. To prevent doctors from ordering tests",
          "C. To delete patient charts older than 15 minutes",
          "D. To restart the database engine"
        ],
        "correct_option": "A",
        "explanation": "Checkpoints flush memory buffers to disk, keeping crash recovery windows short."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why do high-volume banking transaction logs use checkpoints?",
        "options": [
          "A. To flush dirty ledger pages to NVRAM, allowing recovery to avoid reprocessing years of historical log data",
          "B. To disable database encryption",
          "C. To pause all customer ATM access",
          "D. To reset customer account balances"
        ],
        "correct_option": "A",
        "explanation": "Checkpoints bound crash recovery duration by ensuring prior writes are safely on disk."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "What operational purpose do checkpoints serve in high-throughput flash sale databases?",
        "options": [
          "A. Canceling all pending orders",
          "B. Guaranteeing dirty inventory pages are synced to SSDs so recovery scans only need to inspect recent log entries",
          "C. Disabling checkout buttons",
          "D. Lowering product prices by 50%"
        ],
        "correct_option": "B",
        "explanation": "Checkpoints persist dirty pages, drastically cutting recovery time after sudden node failures."
      }
    ]
  },
  {
    "id": "MCQ-068",
    "title": "ER Modeling: Multivalued Attributes & Double Ellipse",
    "topic": "Relational Model & Normalization",
    "subtopic": "Entity-Relationship Diagrams and Attribute Representations",
    "difficulty": "Easy",
    "source": "ISRO CSE 2017 | Question: 8",
    "prompt": "In standard Entity-Relationship (ER) diagram notation (Peter Chen style), what does a 'double ellipse' represent?",
    "options": [
      "A. Key attribute",
      "B. Multivalued attribute",
      "C. Derived attribute",
      "D. Weak entity set"
    ],
    "correct_option": "B",
    "explanation": "In Chen's ER notation: a single ellipse denotes a standard attribute, an underlined ellipse denotes a primary key attribute, a dashed ellipse denotes a derived attribute, a double ellipse denotes a multivalued attribute, and a double rectangle denotes a weak entity.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital ER diagram, where a patient can possess multiple phone numbers or multiple known allergies, how is 'Allergies' drawn?",
        "options": [
          "A. As a double rectangle",
          "B. As a diamond",
          "C. As a double ellipse (multivalued attribute)",
          "D. As a dashed circle"
        ],
        "correct_option": "C",
        "explanation": "Multivalued attributes like multiple allergies are represented with double ellipses."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In banking ER modeling, if a corporate client can have multiple authorized signatory passport numbers, how is 'Signatory_Passports' represented?",
        "options": [
          "A. Double ellipse",
          "B. Solid hexagon",
          "C. Triangle",
          "D. Underlined rectangle"
        ],
        "correct_option": "A",
        "explanation": "Multiple values per entity row are modeled as double ellipses in ER diagrams."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an e-commerce catalog ER diagram, where a fashion product comes in multiple available colors, 'Colors' is drawn as:",
        "options": [
          "A. Single square",
          "B. Double ellipse (multivalued attribute)",
          "C. Dashed diamond",
          "D. Concentric octagons"
        ],
        "correct_option": "B",
        "explanation": "Product colors with multiple entries per item are drawn as double ellipses."
      }
    ]
  },
  {
    "id": "MCQ-069",
    "title": "Candidate Key Minimal Superkey Property",
    "topic": "Relational Model & Normalization",
    "subtopic": "Candidate Key Invariants",
    "difficulty": "Medium",
    "source": "ISRO CSE 2014 | Question: 42",
    "prompt": "What is the formal mathematical definition of a 'Candidate Key' in relational database theory?",
    "options": [
      "A. Any attribute that contains only integer values",
      "B. A minimal superkey (a set of attributes that uniquely identifies every tuple, with no proper subset being a superkey)",
      "C. Any column with an index built on it",
      "D. An attribute that references a primary key in another table"
    ],
    "correct_option": "B",
    "explanation": "A superkey is any attribute set that uniquely identifies tuples. A candidate key is defined as a minimal superkey: it possesses the uniqueness property, and removing any single attribute from it destroys uniqueness (the minimality property).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In hospital records, why is {Patient_SSN, Blood_Type} a superkey but NOT a candidate key?",
        "options": [
          "A. Because removing Blood_Type leaves Patient_SSN which is still unique, violating minimality",
          "B. Because SSN contains hyphens",
          "C. Because blood type is confidential",
          "D. Because doctors do not use SSNs"
        ],
        "correct_option": "A",
        "explanation": "Candidate keys must be minimal; superkeys with redundant extra columns are not candidate keys."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In customer banking, why is {IBAN, Customer_Age} classified as a superkey rather than a candidate key?",
        "options": [
          "A. Because IBAN alone guarantees uniqueness, making Customer_Age a redundant attribute that violates minimality",
          "B. Because age changes every year",
          "C. Because banking tables require three primary keys",
          "D. Because IBANs cannot be stored in databases"
        ],
        "correct_option": "A",
        "explanation": "A candidate key cannot contain unnecessary attributes; IBAN alone is minimal."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In order tracking, why is {Order_Number, Shipping_Zipcode} not a candidate key for table Orders?",
        "options": [
          "A. Zipcodes contain 5 digits",
          "B. Order_Number alone is already unique, so adding Shipping_Zipcode violates the minimality requirement",
          "C. Orders cannot have zipcodes",
          "D. Minimality only applies to view queries"
        ],
        "correct_option": "B",
        "explanation": "A candidate key is a minimal superkey with zero superfluous columns."
      }
    ]
  },
  {
    "id": "MCQ-070",
    "title": "B+ Tree Leaf Node Doubly Linked List Scanning",
    "topic": "Physical Storage & Indexing",
    "subtopic": "B+ Tree Range Query Optimization",
    "difficulty": "Medium",
    "source": "ISRO CSE 2015 | Question: 18",
    "prompt": "In database storage architectures, why is a B+ Tree overwhelmingly preferred over a standard B Tree for relational index structures?",
    "options": [
      "A. B+ Trees do not store keys in internal nodes",
      "B. All data pointers reside in leaf nodes, which are linked together in a sequential linked list enabling efficient range queries (e.g. BETWEEN X AND Y)",
      "C. B+ Trees require no rebalancing upon deletions",
      "D. B+ Trees consume zero memory in the buffer pool"
    ],
    "correct_option": "B",
    "explanation": "In a B+ Tree, internal nodes store only routing search keys, and all actual record pointers reside in leaf nodes. Crucially, all leaf nodes are connected via a doubly linked list, allowing fast sequential scanning for range queries without tree traversals.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When a hospital audits patient admissions 'WHERE Admission_Date BETWEEN 2026-01-01 AND 2026-03-31', how does a B+ tree index execute this efficiently?",
        "options": [
          "A. It finds the start date in O(log N) and then traverses the sequential leaf-node linked list without re-traversing tree branches",
          "B. It scans the hospital disk from sector 0",
          "C. It performs a separate tree traversal for every second in the three months",
          "D. It converts dates into floating point numbers"
        ],
        "correct_option": "A",
        "explanation": "B+ tree linked leaf nodes make sequential range scans exceptionally fast."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In banking ledger queries 'WHERE Tx_Timestamp BETWEEN T1 AND T2', how does the B+ tree avoid random disk seeks?",
        "options": [
          "A. By traversing directly across the linked leaf nodes after navigating to the starting timestamp",
          "B. By eliminating the root node",
          "C. By sorting the database in reverse",
          "D. By caching the entire ledger in L1 CPU cache"
        ],
        "correct_option": "A",
        "explanation": "Leaf-level pointers enable sequential disk block reading for time-series range queries."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "How does a product catalog search for 'WHERE Price BETWEEN $50 AND $100' leverage B+ tree architecture?",
        "options": [
          "A. It calculates hashes for every integer from 50 to 100",
          "B. It seeks to $50 at the leaf level and walks the leaf sibling pointers until exceeding $100",
          "C. It re-indexes the products table on every search",
          "D. It downloads the catalog to the user browser"
        ],
        "correct_option": "B",
        "explanation": "Linked leaf nodes provide optimal sequential I/O for bounded price range searches."
      }
    ]
  },
  {
    "id": "MCQ-071",
    "title": "Dense vs Sparse Secondary Indexing",
    "topic": "Physical Storage & Indexing",
    "subtopic": "Dense and Sparse Index Structures",
    "difficulty": "Medium",
    "source": "ISRO CSE 2017 | Question: 1",
    "prompt": "Which of the following statements about Dense and Sparse database indices is TRUE?",
    "options": [
      "A. A sparse index contains an index entry for every search key value in the data file",
      "B. A dense index contains an index record for every single search key value in the relation, whereas a sparse index contains records for only some search values",
      "C. Sparse indices can be built on un-ordered data files",
      "D. Dense indices cannot be used for primary keys"
    ],
    "correct_option": "B",
    "explanation": "A dense index has an index entry for every search key value in the data file. A sparse index has index entries for only some values (typically one entry per data block), which requires the data file to be physically sorted on that search key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical database, why must a secondary index on Patient_Phone_Number be a DENSE index?",
        "options": [
          "A. Because the underlying data file is sorted by Patient_ID, not phone number; a sparse index cannot find records in unsorted data",
          "B. Because sparse indices are illegal in healthcare",
          "C. Because phone numbers are 10 digits",
          "D. Because dense indices prevent telephone spam"
        ],
        "correct_option": "A",
        "explanation": "Secondary indices on unsorted attributes must be dense to guarantee locateability."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a ledger sorted by Transaction_ID, why can an index on Account_Number NOT be sparse?",
        "options": [
          "A. Because Account_Number is not the physical sort order; only dense secondary indices can locate arbitrary positions",
          "B. Because sparse indices cannot store numbers",
          "C. Because accounts change daily",
          "D. Because bank ledgers must use hash tables only"
        ],
        "correct_option": "A",
        "explanation": "Sparse indices require physical file sorting; secondary search keys require dense indexing."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why must an index on Product_Category in an un-ordered products heap file be dense?",
        "options": [
          "A. Because products have photos",
          "B. Every product category must have an index entry because the heap file is not sorted by category",
          "C. To prevent duplicate categories",
          "D. Because sparse indices take more disk space"
        ],
        "correct_option": "B",
        "explanation": "Dense indices maintain pointers for every key value across unsorted heap files."
      }
    ]
  },
  {
    "id": "MCQ-072",
    "title": "Data Integrity Enforcement: Constraints vs Triggers",
    "topic": "Triggers & Active Databases",
    "subtopic": "Declarative Constraints vs Procedural Triggers",
    "difficulty": "Medium",
    "source": "NIELIT 2021 Dec Scientist B - Section B: 9",
    "prompt": "Specify, which of the following is the preferred method for enforcing data integrity in a relational database?",
    "options": [
      "A. Constraints",
      "B. Stored procedure",
      "C. Triggers",
      "D. Cursors"
    ],
    "correct_option": "A",
    "explanation": "Declarative database constraints (PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE, NOT NULL) are preferred over triggers because they are declarative, self-documenting, and heavily optimized by the query planner. Procedural triggers are reserved for complex cross-table business logic.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When enforcing that a patient body temperature must lie between 30°C and 45°C, what is the preferred mechanism in a clinical database?",
        "options": [
          "A. An external Python stored procedure",
          "B. A declarative CHECK constraint directly on the Vitals table",
          "C. An asynchronous daily trigger",
          "D. A database cursor"
        ],
        "correct_option": "B",
        "explanation": "Declarative CHECK constraints are faster, safer, and preferred over procedural code for simple range invariants."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "To enforce that savings account balances must never drop below the $500 minimum balance, what is the best database approach?",
        "options": [
          "A. Manual verification by tellers",
          "B. An uncompiled stored procedure",
          "C. A table-level declarative CHECK (Balance >= 500) constraint",
          "D. A database view with no base table"
        ],
        "correct_option": "C",
        "explanation": "Declarative constraints are built into the relational engine and execute with zero procedural overhead."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To ensure product discount percentages never exceed 90%, which database method is preferred?",
        "options": [
          "A. A statement-level trigger",
          "B. A client-side JavaScript regex only",
          "C. A database cursor loop",
          "D. A declarative CHECK (discount_pct <= 90) constraint"
        ],
        "correct_option": "D",
        "explanation": "Declarative constraints provide guaranteed engine-level integrity without trigger complexity."
      }
    ]
  },
  {
    "id": "MCQ-073",
    "title": "Lock Synchronization in Concurrent Database Systems",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Global vs Local Locks",
    "difficulty": "Medium",
    "source": "NIELIT 2016 MAR Scientist B - Section C: 34",
    "prompt": "In distributed and multi-tier database systems, what is the primary function of Global Locks?",
    "options": [
      "A. Synchronize access to local resources exclusively within a single CPU core",
      "B. Synchronize access to global, shared resources across distributed database instances",
      "C. Are used to avoid local locks entirely",
      "D. Prevent all read access permanently across all nodes"
    ],
    "correct_option": "B",
    "explanation": "Global locks coordinate access to resources distributed across multiple cluster nodes or instances, preventing conflicting concurrent updates and ensuring serializability across the distributed cluster.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital network where three surgical centers share an organ donor allocation catalog, why are global locks used?",
        "options": [
          "A. To synchronize access to available donor organs across all surgical centers, preventing double allocation",
          "B. To prevent local nurses from logging in",
          "C. To delete patient histories automatically",
          "D. To avoid local memory usage"
        ],
        "correct_option": "A",
        "explanation": "Global locks synchronize shared organ inventory across distinct hospital nodes."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a distributed global payment network across Tokyo, London, and New York, why are global locks managed by the transaction coordinator?",
        "options": [
          "A. To synchronize multi-currency settlement ledgers across geographical regions",
          "B. To replace database passwords",
          "C. To make transactions unrecoverable",
          "D. To slow down international banking"
        ],
        "correct_option": "A",
        "explanation": "Global locking prevents conflicting concurrent postings to shared international ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a global inventory system where regional warehouses fulfill orders from a central master stock, what do global locks guarantee?",
        "options": [
          "A. Elimination of customer shipping costs",
          "B. Coordinated, conflict-free stock allocation across all fulfillment centers",
          "C. Faster website image loading",
          "D. Unlimited checkout attempts"
        ],
        "correct_option": "B",
        "explanation": "Global locks prevent race conditions on shared master stock across distributed nodes."
      }
    ]
  },
  {
    "id": "MCQ-074",
    "title": "Irrecoverable Error Anomaly: Dirty Read followed by Uncommitted Write",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Irrecoverable Schedules and Dirty Reads",
    "difficulty": "Hard",
    "source": "NIELIT 2022 April Scientist B | Section B | Question: 58",
    "prompt": "Which of the following transaction execution scenarios leads to an IRRECOVERABLE error in a database system?",
    "options": [
      "A. A transaction writes a data item after it is read by an uncommitted transaction",
      "B. A transaction reads a data item after it is read by an uncommitted transaction",
      "C. A transaction reads a data item after it is written by a committed transaction",
      "D. A transaction reads a data item after it is written by an uncommitted transaction, and then commits before the writing transaction commits"
    ],
    "correct_option": "D",
    "explanation": "A schedule is irrecoverable if transaction T2 reads dirty data written by uncommitted transaction T1, and T2 commits before T1. If T1 subsequently aborts, T2 cannot be rolled back because it has already committed (durability), leaving corrupted data in the database.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Doctor T2 reads an uncommitted insulin dosage entered by Doctor T1. T2 commits and prints the discharge order. T1 then aborts due to an allergic warning. Why is this an irrecoverable error?",
        "options": [
          "A. Because the printer ran out of paper",
          "B. Because T2 already committed and discharged the patient based on an aborted, non-existent insulin order",
          "C. Because insulin is an injectable medication",
          "D. Because T1 and T2 used the same hospital terminal"
        ],
        "correct_option": "A",
        "explanation": "Committed dirty reads produce irrecoverable real-world states when the parent aborts."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Wire transfer T2 reads an uncommitted $100K credit posted by T1. T2 commits and wires the funds externally. T1 then aborts due to fraud. Why is the database in an irrecoverable state?",
        "options": [
          "A. T2 committed and paid out cash based on a phantom credit that was rolled back",
          "B. Foreign exchange markets closed",
          "C. The bank accounts were deleted",
          "D. Interest rates decreased"
        ],
        "correct_option": "A",
        "explanation": "Irrecoverable schedules violate financial durability when uncommitted dirty writes abort after downstream commit."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Cart T2 reads an uncommitted price discount of $1 posted by promotional batch T1. T2 commits and completes payment. T1 aborts. Why is this schedule irrecoverable?",
        "options": [
          "A. T2 committed a purchase using a discount that was rolled back and never officially existed",
          "B. The customer returned the item",
          "C. Products cannot be discounted",
          "D. Inventory was out of stock"
        ],
        "correct_option": "B",
        "explanation": "Premature commit of dirty-read data creates irrecoverable transactional anomalies."
      }
    ]
  },
  {
    "id": "MCQ-075",
    "title": "Relational Lossless Join & Dependency Preservation",
    "topic": "Relational Model & Normalization",
    "subtopic": "Decomposition Properties and Functional Dependencies",
    "difficulty": "Medium",
    "source": "NIELIT 2022 April Scientist B | Section B | Question: 49",
    "prompt": "Let R(A, B, C, D) be a relational schema with functional dependencies F = {A -> B, B -> C, C -> D}. The decomposition of R into R1(A, B), R2(B, C), and R3(C, D):",
    "options": [
      "A. Gives a lossless join, and is dependency preserving",
      "B. Gives a lossless join, but is not dependency preserving",
      "C. Does not give a lossless join, but is dependency preserving",
      "D. Does not give a lossless join and is not dependency preserving"
    ],
    "correct_option": "A",
    "explanation": "A decomposition has a lossless join if the intersection of joined relations contains a candidate key of at least one of them. R1 ∩ R2 = B (key for R2 since B->C), and (R1 ⨝ R2) ∩ R3 = C (key for R3 since C->D). All original dependencies (A->B, B->C, C->D) are explicitly preserved within the decomposed relations.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Decomposing Patient_Diagnosis(Patient_ID, Symptom_Code, Disease_Code, Treatment_Code) with chain dependencies into 3 pairwise relations achieves:",
        "options": [
          "A. Loss of medical diagnosis records",
          "B. A lossless join and full dependency preservation",
          "C. An irrecoverable patient state",
          "D. Violations of 1NF"
        ],
        "correct_option": "B",
        "explanation": "Chained pairwise decomposition along dependency edges preserves dependencies losslessly."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Decomposing Bank_Facility(Loan_ID, Borrower_ID, Credit_Score, Interest_Rate) along functional dependencies into R1, R2, R3:",
        "options": [
          "A. Erases credit history",
          "B. Doubles interest rates",
          "C. Guarantees a lossless join and preserves all banking regulatory dependencies",
          "D. Fails 2NF requirements"
        ],
        "correct_option": "C",
        "explanation": "Intersection attributes contain superkeys of components, ensuring lossless reconstruction."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce supply chain normalization, decomposing SKU_Supply along {SKU->Vendor, Vendor->City, City->Tax} into 3 sub-relations:",
        "options": [
          "A. Causes missing product descriptions",
          "B. Fails BCNF standards",
          "C. Increases network latency by 500%",
          "D. Is both lossless-join and dependency-preserving"
        ],
        "correct_option": "D",
        "explanation": "The decomposition preserves all dependencies and guarantees lossless relational reconstruction."
      }
    ]
  },
  {
    "id": "MCQ-076",
    "title": "Highest Normal Form Determination under Functional Dependencies",
    "topic": "Relational Model & Normalization",
    "subtopic": "Normal Form Hierarchy (1NF, 2NF, 3NF, BCNF)",
    "difficulty": "Hard",
    "source": "NIELIT 2022 April Scientist B | Section B | Question: 54",
    "prompt": "Given relation R(Name, Course_No, Roll_No, Grade) with functional dependencies: {Name, Course_No -> Grade; Roll_No, Course_No -> Grade; Name -> Roll_No; Roll_No -> Name}. What is the HIGHEST normal form of R?",
    "options": [
      "A. 1NF",
      "B. 2NF",
      "C. 3NF",
      "D. BCNF"
    ],
    "correct_option": "C",
    "explanation": "Candidate keys are {Name, Course_No} and {Roll_No, Course_No}. Prime attributes are {Name, Course_No, Roll_No}. In Name -> Roll_No, Name is not a superkey, violating BCNF. However, Roll_No is a prime attribute, which satisfies the 3NF condition. Hence, R is in 3NF.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In Medical_Trial(Doctor_Name, Trial_ID, License_No, Outcome) where Name and License are interchangeable candidate keys with Trial_ID, what normal form is achieved?",
        "options": [
          "A. 1NF only",
          "B. 2NF only",
          "C. BCNF",
          "D. 3NF (because non-superkey determinants map to prime attributes)"
        ],
        "correct_option": "A",
        "explanation": "When the RHS of a non-superkey dependency is a prime attribute, the relation satisfies 3NF but not BCNF."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In Trader_Account(Trader_Email, Asset_ID, Tax_ID, Trade_Limit) where Trader_Email <-> Tax_ID: what is the highest normal form?",
        "options": [
          "A. 3NF",
          "B. 1NF",
          "C. 2NF",
          "D. BCNF"
        ],
        "correct_option": "A",
        "explanation": "The relation is in 3NF because Tax_ID is prime; it fails BCNF because Email is not a superkey alone."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In Vendor_Contract(Vendor_Slug, Category_ID, Vendor_DUNS, Commission_Rate): what is the highest normal form?",
        "options": [
          "A. 1NF",
          "B. 3NF",
          "C. 2NF",
          "D. BCNF"
        ],
        "correct_option": "B",
        "explanation": "Satisfies 3NF as prime attributes appear on RHS; fails BCNF due to partial candidate key determinants."
      }
    ]
  },
  {
    "id": "MCQ-077",
    "title": "Self-Join and Unary Relationship Querying",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Self-Joins on Hierarchical Schemas",
    "difficulty": "Easy",
    "source": "NIELIT 2017 July Scientist B (IT) - Section B: 55",
    "prompt": "A table joined with itself in an SQL query is formally referred to as a:",
    "options": [
      "A. Natural Join",
      "B. Self Join",
      "C. Outer Join",
      "D. Equi Join"
    ],
    "correct_option": "B",
    "explanation": "A Self Join is a regular join in which a table is joined with itself using distinct table aliases (e.g. Employee E1 JOIN Employee E2 ON E1.Manager_ID = E2.Emp_ID) to query recursive or hierarchical relationships.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "To match each hospital resident with their supervising attending physician stored in the same Doctors table, what SQL join is executed?",
        "options": [
          "A. Cross Join",
          "B. Full Outer Union",
          "C. Self Join (Doctors D1 JOIN Doctors D2 ON D1.Supervisor_ID = D2.Doc_ID)",
          "D. Semi-join"
        ],
        "correct_option": "A",
        "explanation": "Self-joins resolve parent-child supervision hierarchies within a single clinical table."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "To query banking accounts alongside their designated backup guarantee accounts from the same Accounts table, which SQL technique is used?",
        "options": [
          "A. Self Join using distinct table aliases for primary and backup accounts",
          "B. Group by rollup",
          "C. Drop view",
          "D. Truncate table"
        ],
        "correct_option": "A",
        "explanation": "Self-joins compare rows within the same financial entity relation."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To query categories alongside their parent categories from a unified Categories table, the database uses:",
        "options": [
          "A. A Cartesian product with no aliases",
          "B. A Self Join",
          "C. A database trigger",
          "D. An unlogged cursor"
        ],
        "correct_option": "B",
        "explanation": "Self joins evaluate recursive hierarchical links in catalog schemas."
      }
    ]
  },
  {
    "id": "MCQ-078",
    "title": "Hash File Addressing & Record Location Transformation",
    "topic": "Physical Storage & Indexing",
    "subtopic": "Hash Addressing and Bucket Capacity",
    "difficulty": "Easy",
    "source": "NIELIT Scientist B 2020 November: 103",
    "prompt": "The physical storage organization where the location of a record is determined by a mathematical formula that transforms a search key into an address block is known as:",
    "options": [
      "A. B-Tree File",
      "B. Hashed File (Hash-based indexing)",
      "C. Indexed-Sequential File",
      "D. Heap File"
    ],
    "correct_option": "B",
    "explanation": "In hash file organizations, a hash function h(K) applies a mathematical transformation to search key K to directly compute the bucket address on disk, enabling average O(1) direct record lookups.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A clinical genetic database maps 3-billion-base-pair genomic variant IDs directly into storage addresses using a hash function. What file organization is this?",
        "options": [
          "A. B-Tree file",
          "B. Unsorted text document",
          "C. Hashed file organization",
          "D. Magnetic tape spool"
        ],
        "correct_option": "A",
        "explanation": "Hash file organizations transform keys directly to bucket addresses."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A credit card payment authorization switch looks up card account metadata in sub-millisecond time by applying a mathematical function to the 16-digit PAN. This storage structure is a:",
        "options": [
          "A. Hashed file",
          "B. Circular queue",
          "C. Binary heap",
          "D. Linear sequential tape"
        ],
        "correct_option": "A",
        "explanation": "Hash-based addressing computes direct bucket addresses for low-latency lookups."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "A session store maps buyer HTTP cookie tokens directly into memory cache buckets using a cryptographic hash. This is an example of:",
        "options": [
          "A. Sequential punch-card indexing",
          "B. Hash-addressed file storage",
          "C. Bubble-sorted array",
          "D. Depth-first search tree"
        ],
        "correct_option": "B",
        "explanation": "Hash files transform keys into address offsets for rapid key-value retrieval."
      }
    ]
  },
  {
    "id": "MCQ-079",
    "title": "Role Permissions and Access Control Rights",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role-Based Access Control and Privilege Grants",
    "difficulty": "Medium",
    "source": "NIELIT 2017 OCT Scientific Assistant A - Section B: 54",
    "prompt": "In SQL Role-Based Access Control (RBAC), what is the primary architectural advantage of granting database privileges to 'ROLES' rather than directly to individual user accounts?",
    "options": [
      "A. It reduces disk storage consumption by 90%",
      "B. It simplifies privilege administration by decoupling user identities from access rights, allowing users to inherit permissions dynamically as their job roles change",
      "C. It disables all database logging to maximize throughput",
      "D. It eliminates the need for user passwords"
    ],
    "correct_option": "B",
    "explanation": "Role-Based Access Control (RBAC) maps permissions to named roles (e.g. 'auditor', 'teller', 'pharmacist') rather than individual users. Users are assigned roles, making access administration scalable, maintainable, and compliant with the Principle of Least Privilege.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why does a hospital database define roles like 'Attending_Physician' and 'Triage_Nurse' rather than granting table rights directly to Dr. Robert Smith?",
        "options": [
          "A. When Dr. Smith leaves or rotates wards, simply revoking his role membership revokes all chart privileges without reconfiguring individual table permissions",
          "B. To prevent doctors from accessing medical equipment",
          "C. Because medical regulations forbid using doctor names in databases",
          "D. To encrypt database backups"
        ],
        "correct_option": "A",
        "explanation": "RBAC decouples permission grants from user accounts, streamlining clinical staff turnover."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why do banking core systems assign 'Branch_Manager' roles rather than granting override privileges to individual employees?",
        "options": [
          "A. Centralized role management enforces uniform compliance policies and prevents orphaned privilege drift",
          "B. Because tellers share a single computer terminal",
          "C. To eliminate transaction audit logs",
          "D. To avoid paying database license fees"
        ],
        "correct_option": "A",
        "explanation": "RBAC ensures consistent permission governance across thousands of branch employees."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a marketplace platform, why are permissions granted to roles like 'Fulfillment_Agent' and 'Customer_Service'?",
        "options": [
          "A. To prevent customers from seeing product prices",
          "B. Scalable user-to-role assignment ensures support staff only inherit rights required for their specific operational duties",
          "C. Because roles bypass SSL certificates",
          "D. To automatically refund orders"
        ],
        "correct_option": "B",
        "explanation": "Role-based authorization prevents permission leakage and enforces least privilege."
      }
    ]
  },
  {
    "id": "MCQ-080",
    "title": "ER Diagram Weak Entity Representation",
    "topic": "Relational Model & Normalization",
    "subtopic": "Weak Entity Sets and Identifying Relationships",
    "difficulty": "Easy",
    "source": "NIELIT 2021 Dec Scientist A - Section B: 49",
    "prompt": "In an Entity-Relationship (ER) diagram, how are a 'Weak Entity Set' and its 'Identifying Relationship' visually represented?",
    "options": [
      "A. Single rectangle and single diamond",
      "B. Double rectangle (weak entity) and double diamond (identifying relationship)",
      "C. Double ellipse and single rectangle",
      "D. Dashed circle and underlined rectangle"
    ],
    "correct_option": "B",
    "explanation": "In Chen ER notation, a weak entity set (which lacks a primary key of its own and depends on an owner entity) is represented by a doubly outlined rectangle. Its identifying relationship with the owner entity is represented by a doubly outlined diamond.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In hospital modeling, Dependent_Family_Member has no independent primary key and relies on Employee_Nurse. How is Dependent_Family_Member drawn?",
        "options": [
          "A. As a double rectangle connected via a double diamond",
          "B. As a solid hexagon",
          "C. As a dotted circle",
          "D. As an inverted triangle"
        ],
        "correct_option": "A",
        "explanation": "Weak entity sets are depicted as double rectangles in ER diagrams."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In banking, Cheque_Leaf has no globally unique ID and depends on Account_Number. How is Cheque_Leaf represented?",
        "options": [
          "A. Double rectangle connected to Account via double diamond identifying relationship",
          "B. Bold ellipse",
          "C. Concentric circles",
          "D. Single square with no borders"
        ],
        "correct_option": "A",
        "explanation": "Cheque leaf records are weak entities drawn with double rectangles."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an order management ER diagram, Order_Line_Item relies on Order_ID for uniqueness. Order_Line_Item is drawn as:",
        "options": [
          "A. A single dashed ellipse",
          "B. A double rectangle with a double diamond identifying relationship",
          "C. A solid black circle",
          "D. A triple-line triangle"
        ],
        "correct_option": "B",
        "explanation": "Line items depending on parent order IDs are classic weak entities modeled as double rectangles."
      }
    ]
  },
  {
    "id": "MCQ-081",
    "title": "Referential Integrity Violation under Child Insertions",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Foreign Key Insertion Invariants",
    "difficulty": "Medium",
    "source": "NIELIT 2018 | Question: 49",
    "prompt": "In a database with Parent table P(P_ID PRIMARY KEY) and Child table C(C_ID PRIMARY KEY, P_ID REFERENCES P(P_ID)), which operation is GUARANTEED to cause a referential integrity violation if not properly checked?",
    "options": [
      "A. Inserting a new tuple into Parent table P",
      "B. Inserting a new tuple into Child table C with a P_ID value that does not exist in P",
      "C. Deleting a tuple from Child table C",
      "D. Querying Parent table P with a SELECT statement"
    ],
    "correct_option": "B",
    "explanation": "Referential integrity is violated if a child tuple contains a foreign key value referencing a parent key that does not exist in the referenced table. Inserting into parent P or deleting from child C can never violate foreign key referential integrity.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical database, what operation triggers an immediate foreign key constraint violation?",
        "options": [
          "A. Inserting a prescription record referencing Patient_ID = 9999 when patient 9999 is not registered in Patients",
          "B. Discharging an inpatient",
          "C. Registering a new doctor",
          "D. Querying doctor names"
        ],
        "correct_option": "A",
        "explanation": "Inserting child records referencing non-existent parent IDs violates referential integrity."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a core banking system, what causes an immediate referential integrity error?",
        "options": [
          "A. Posting a wire transfer referencing Account_Number 'ACC-999' when ACC-999 does not exist in Accounts",
          "B. Paying interest to an account",
          "C. Running a balance audit",
          "D. Opening a new checking account"
        ],
        "correct_option": "A",
        "explanation": "Transactions referencing non-existent accounts violate foreign key invariants."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "What causes an immediate foreign key constraint rejection during checkout?",
        "options": [
          "A. Adding a new product to the catalog",
          "B. Inserting an order item with Product_SKU = 'SKU-UNKNOWN' not present in the master Products table",
          "C. Canceling an order",
          "D. Updating user password"
        ],
        "correct_option": "B",
        "explanation": "Referencing non-existent product keys triggers foreign key rejection."
      }
    ]
  },
  {
    "id": "MCQ-082",
    "title": "Foreign Key Constraints with ON DELETE CASCADE Semantics",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Cascade Deletion Execution Patterns",
    "difficulty": "Medium",
    "source": "NIELIT 2021 Dec Scientist B - Section B: 10",
    "prompt": "When defining a foreign key with 'ON DELETE CASCADE' in an SQL DDL statement, what action is executed by the DBMS engine when a referenced primary key tuple is deleted?",
    "options": [
      "A. The delete is rejected and an error is thrown",
      "B. All matching child tuples referencing that primary key are automatically deleted in the same transaction",
      "C. Foreign key columns in matching child rows are updated to 0",
      "D. The parent table is truncated"
    ],
    "correct_option": "B",
    "explanation": "ON DELETE CASCADE specifies that when a row in the parent table is deleted, all referencing rows in child tables are automatically deleted by the database engine as an internal referential action, maintaining referential integrity without orphan records.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When a patient record is purged from Patients with ON DELETE CASCADE enabled on Medical_History(Patient_ID):",
        "options": [
          "A. All corresponding medical history records for that patient are automatically deleted",
          "B. Patient records are copied to the pharmacy",
          "C. The deletion throws a fatal database crash",
          "D. Medical history is preserved with Patient_ID set to -1"
        ],
        "correct_option": "A",
        "explanation": "ON DELETE CASCADE purges dependent medical history rows automatically."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If an account profile is purged with ON DELETE CASCADE on Account_Beneficiaries(Account_ID):",
        "options": [
          "A. All registered beneficiaries linked to that account are automatically deleted",
          "B. The account is moved to savings",
          "C. The operation is blocked",
          "D. Beneficiaries receive a wire transfer"
        ],
        "correct_option": "A",
        "explanation": "Cascading deletes purge dependent beneficiary tuples automatically."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an abandoned cart is deleted from Cart with ON DELETE CASCADE on Cart_Items(Cart_ID):",
        "options": [
          "A. All warehouse products are deleted",
          "B. All item records inside that cart are automatically removed from Cart_Items",
          "C. Cart items are shipped to customer",
          "D. An error is returned"
        ],
        "correct_option": "B",
        "explanation": "ON DELETE CASCADE cleans up dependent cart item rows without manual deletes."
      }
    ]
  },
  {
    "id": "MCQ-083",
    "title": "Entity Integrity Constraint: Non-Null Primary Keys",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Entity Integrity and Primary Key Non-Nullness",
    "difficulty": "Easy",
    "source": "NIELIT Scientific Assistant A 2020 November: 97",
    "prompt": "The 'Entity Integrity Constraint' in the relational model mandates that:",
    "options": [
      "A. Foreign key values must match primary key values",
      "B. No primary key attribute (or component of a composite primary key) may contain a NULL value",
      "C. Secondary indices must be dense",
      "D. Table names must be unique across the schema"
    ],
    "correct_option": "B",
    "explanation": "Entity Integrity is a core relational model rule stating that every base relation must have a primary key, and no primary key attribute may be NULL. Because primary keys serve as unique tuple locators, allowing NULL would prevent uniquely identifying individual entities.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In hospital records, why does the database reject creating a Patient record with Patient_ID = NULL?",
        "options": [
          "A. It violates the Entity Integrity Constraint, which strictly forbids NULL primary keys",
          "B. Because patient IDs must be negative",
          "C. Because NULL is reserved for doctor names",
          "D. Because medical databases only support integer types"
        ],
        "correct_option": "A",
        "explanation": "Entity integrity dictates that primary keys cannot be NULL."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why is 'INSERT INTO Accounts(Account_Number, Balance) VALUES (NULL, 1000)' rejected by Oracle and PostgreSQL?",
        "options": [
          "A. It violates Entity Integrity because primary key Account_Number cannot be NULL",
          "B. Because interest is not calculated",
          "C. Because currency was not specified",
          "D. Because the balance is too low"
        ],
        "correct_option": "A",
        "explanation": "Primary keys must be non-null to uniquely identify account entities."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why cannot an e-commerce platform insert an Order with Order_ID = NULL?",
        "options": [
          "A. Because credit cards reject null numbers",
          "B. Entity integrity prohibits null primary keys to ensure every order is uniquely addressable",
          "C. Because orders must have tracking numbers",
          "D. Because carts are temporary tables"
        ],
        "correct_option": "B",
        "explanation": "Entity integrity requires primary keys to be unique and strictly non-null."
      }
    ]
  },
  {
    "id": "MCQ-084",
    "title": "Relational Foreign Key Domain Compatibility",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Foreign Key Type Compatibility Rules",
    "difficulty": "Easy",
    "source": "NIELIT 2016 MAR Scientist B - Section C: 41",
    "prompt": "When establishing a foreign key relationship between Child(A) and Parent(B), what is the mandatory structural requirement on attributes A and B?",
    "options": [
      "A. Attribute A and Attribute B must have compatible data types and identical domains",
      "B. Attribute A must have twice the byte length of Attribute B",
      "C. Attributes A and B must share the same column name in both tables",
      "D. Both tables must reside on the same physical hard disk partition"
    ],
    "correct_option": "A",
    "explanation": "A foreign key constraint requires that the referencing attribute and the referenced candidate key attribute share compatible data types and domain definitions (e.g., both must be INT, or both VARCHAR of compatible length) so values can be compared for referential equality.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If Patients(Patient_ID) is defined as UUID, why does defining Prescriptions(Patient_ID) as INT throw a DDL creation error?",
        "options": [
          "A. Because UUID is not supported in healthcare",
          "B. Because foreign key and referenced key attributes must share compatible data types and domains",
          "C. Because prescriptions cannot reference patients",
          "D. Because table names must start with capital letters"
        ],
        "correct_option": "B",
        "explanation": "Foreign key relationships require matching data types across referenced attributes."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why can a VARCHAR(34) IBAN foreign key not reference a BIGINT Account_ID primary key?",
        "options": [
          "A. Because IBANs contain country codes",
          "B. Because banks cannot store characters",
          "C. Incompatible data types prevent relational equality matching across foreign key domains",
          "D. Because BIGINT cannot be indexed"
        ],
        "correct_option": "C",
        "explanation": "Foreign keys mandate domain and data type compatibility with referenced keys."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why must Order_Items(Product_SKU) match the exact data type of Products(Product_SKU)?",
        "options": [
          "A. To avoid converting SKU to price",
          "B. To prevent products from being returned",
          "C. Because foreign keys cannot reference text",
          "D. Relational integrity requires matching domains for foreign key constraint validation"
        ],
        "correct_option": "D",
        "explanation": "Matching data types are mandatory for foreign key constraint creation."
      }
    ]
  },
  {
    "id": "MCQ-085",
    "title": "Deadlock Avoidance: Wait-Die vs Wound-Wait Preemption",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Non-preemptive vs Preemptive Timestamp Deadlock Schemes",
    "difficulty": "Medium",
    "source": "NIELIT 2017 OCT Scientific Assistant A (IT): 72",
    "prompt": "Between the two timestamp-based deadlock prevention algorithms 'Wait-Die' and 'Wound-Wait', which one is classified as a NON-PREEMPTIVE scheme?",
    "options": [
      "A. Wound-Wait",
      "B. Wait-Die (because an older transaction is allowed to wait, and younger transactions die without preempting the lock holder)",
      "C. Both schemes are non-preemptive",
      "D. Neither scheme uses timestamps"
    ],
    "correct_option": "B",
    "explanation": "Wait-Die is non-preemptive: an older transaction requesting a resource held by a younger transaction is permitted to wait; a younger transaction requesting from an older transaction immediately dies (aborts itself). In contrast, Wound-Wait is preemptive.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Under Wait-Die in a hospital records engine, what happens when a young routine billing transaction T2 requests patient vitals locked by older surgery transaction T1?",
        "options": [
          "A. T2 dies immediately without preempting T1 (non-preemptive)",
          "B. Both transactions wait in a deadlock cycle",
          "C. T2 aborts T1",
          "D. T1 is demoted"
        ],
        "correct_option": "A",
        "explanation": "In Wait-Die, younger requesting transactions die, ensuring non-preemptive execution."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why is Wait-Die described as non-preemptive in interbank transaction engines?",
        "options": [
          "A. Because transactions never forcibly confiscate locks held by other running transactions",
          "B. Because timestamps are randomized",
          "C. Because locks are granted to all transactions simultaneously",
          "D. Because wire transfers cannot be canceled"
        ],
        "correct_option": "A",
        "explanation": "Non-preemptive schemes never abort the current lock holder."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Under Wait-Die, what occurs when a newly arrived cart T2 requests stock locked by an older cart T1?",
        "options": [
          "A. T2 forcibly preempts T1's lock",
          "B. T2 aborts and dies immediately",
          "C. Both carts merge",
          "D. Inventory is doubled"
        ],
        "correct_option": "B",
        "explanation": "Younger requesting transactions die in Wait-Die rather than preempting older locks."
      }
    ]
  },
  {
    "id": "MCQ-086",
    "title": "ACID Atomicity Rollback Guarantee",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Transaction Abort and Rollback Invariants",
    "difficulty": "Easy",
    "source": "NIELIT 2021 Dec Scientist B - Section B: 78",
    "prompt": "When a database transaction aborts before reaching its commit point, the Atomicity property guarantees that:",
    "options": [
      "A. All changes made by the transaction are rolled back and undone, restoring the database to its pre-transaction state",
      "B. Only the last SQL query is reversed",
      "C. The database is restored to a random state",
      "D. The user's account is permanently deleted"
    ],
    "correct_option": "A",
    "explanation": "Atomicity requires that all operations within a transaction succeed completely, or if any failure occurs prior to commit, all partial updates are completely rolled back and erased, leaving the database exactly as it was before the transaction began.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When a drug dispensing transaction aborts due to an allergic contraindication check, Atomicity guarantees:",
        "options": [
          "A. The patient is marked as deceased",
          "B. All dosage updates and pharmacy inventory deductions are completely rolled back",
          "C. Half the medication is dispensed",
          "D. The hospital server reboots"
        ],
        "correct_option": "B",
        "explanation": "Atomicity guarantees all uncommitted medical updates are rolled back upon abort."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If an ATM power fails during a cash withdrawal after debiting the account but before ejecting cash, Atomicity ensures:",
        "options": [
          "A. The customer loses the money permanently",
          "B. The bank balance becomes negative",
          "C. The debit is rolled back, restoring the customer's original account balance",
          "D. ATM prints a blank paper"
        ],
        "correct_option": "C",
        "explanation": "Atomicity guarantees partial debits roll back if withdrawal fails to complete."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When a shopping cart checkout fails during credit card authorization, what does Atomicity guarantee?",
        "options": [
          "A. The customer is charged twice",
          "B. The product is deleted from the store",
          "C. Delivery is marked as completed",
          "D. Decremented inventory counts and shipping tickets are rolled back to pre-checkout values"
        ],
        "correct_option": "D",
        "explanation": "Atomicity ensures failed checkouts leave inventory states completely uncorrupted."
      }
    ]
  },
  {
    "id": "MCQ-087",
    "title": "Stored Procedure Compilation & Pre-Compiled Execution Plans",
    "topic": "Triggers & Active Databases",
    "subtopic": "Stored Procedures vs Dynamic SQL",
    "difficulty": "Medium",
    "source": "NIELIT 2018 | Question: 34",
    "prompt": "What is a primary performance advantage of executing database operations via 'Stored Procedures' compared to sending ad-hoc dynamic SQL queries from an application?",
    "options": [
      "A. Stored procedures run without database transactions",
      "B. Stored procedures are parsed, optimized, and compiled once on the database server, reusing cached query execution plans and reducing network round-trips",
      "C. Stored procedures store all data in CPU cache permanently",
      "D. Stored procedures bypass SQL syntax checking"
    ],
    "correct_option": "B",
    "explanation": "Stored procedures reside on the database server where they are parsed, analyzed, and compiled once into an optimized query execution plan. Re-executing a stored procedure reuses the cached plan and executes multiple SQL statements in a single network round-trip.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why do hospital EMR systems execute complex surgical admission workflows through a database Stored Procedure rather than individual client queries?",
        "options": [
          "A. It minimizes network round-trips between the operating room terminal and server while reusing pre-compiled query plans",
          "B. To prevent doctors from writing medical notes",
          "C. Because surgical applications cannot format SQL strings",
          "D. Because stored procedures eliminate the need for primary keys"
        ],
        "correct_option": "A",
        "explanation": "Stored procedures bundle multi-step hospital admissions into a single optimized server execution."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why do high-frequency banking settlement engines encapsulate wire transfer logic inside Stored Procedures?",
        "options": [
          "A. To execute balance checks, debit, credit, and audit logging in a single compiled round-trip with minimal latency",
          "B. To bypass double-entry bookkeeping rules",
          "C. Because stored procedures run on client smartphones",
          "D. Because banks are forbidden from using SQL"
        ],
        "correct_option": "A",
        "explanation": "Pre-compiled stored procedures minimize latency and network overhead in financial transfers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "How does using a Stored Procedure optimize flash sale checkout processing?",
        "options": [
          "A. It allows customers to pay with expired cards",
          "B. It validates stock, decrements inventory, and creates order records in one atomic server call using a cached execution plan",
          "C. It disables database locking",
          "D. It removes the need for web servers"
        ],
        "correct_option": "B",
        "explanation": "Stored procedures combine multiple cart operations into a pre-compiled, high-throughput routine."
      }
    ]
  },
  {
    "id": "MCQ-088",
    "title": "Master-Slave Flip-Flop Clock Triggering",
    "topic": "Digital Logic: Flip-Flops & Hardware Triggers",
    "subtopic": "Master-Slave Clock Edge Invariants",
    "difficulty": "Medium",
    "source": "NIELIT 2016 MAR Scientist C - Section C: 41",
    "prompt": "How does a Master-Slave J-K flip-flop eliminate the race-around condition that plagues level-sensitive J-K flip-flops when J=1 and K=1?",
    "options": [
      "A. By isolating input sampling to the Master on clock high, and transferring output to the Slave only on the falling clock edge",
      "B. By replacing J-K gates with D latches",
      "C. By eliminating the clock signal entirely",
      "D. By running on direct current battery power"
    ],
    "correct_option": "A",
    "explanation": "In a Master-Slave J-K flip-flop, the master latch is active when clock is high (sampling J and K inputs), but the slave latch is disabled by an inverter. When the clock falls, the master is disabled and the slave is enabled, transferring the state to output Q once per clock cycle, eliminating race-around.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an implanted medical telemetry clock generator, why is a Master-Slave flip-flop topology used for frequency division?",
        "options": [
          "A. To allow the patient to adjust clock frequencies with a magnet",
          "B. To eliminate race-around toggling errors during high clock phases, ensuring stable biomedical pulse counting",
          "C. Because medical circuits cannot use transistors",
          "D. To double electrical power consumption"
        ],
        "correct_option": "B",
        "explanation": "Master-slave isolation ensures deterministic pulse division without race-around oscillations."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In high-speed cryptographic hashing hardware, why do register dividers use Master-Slave flip-flops?",
        "options": [
          "A. To decrypt passwords in zero clock cycles",
          "B. To allow asynchronous bank wires",
          "C. To sample on clock high and transfer on clock low, preventing uncontrolled multi-toggling in clock cycles",
          "D. Because single flip-flops cannot store bits"
        ],
        "correct_option": "C",
        "explanation": "Master-slave timing guarantees clean state transitions during cryptographic operations."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In automated barcode optical reader timing circuits, why are Master-Slave flip-flops preferred for counter stages?",
        "options": [
          "A. They speed up barcode scanning by 1000x",
          "B. They convert barcodes to QR codes",
          "C. They operate without a power supply",
          "D. They guarantee glitch-free binary counting by isolating input sampling from output updates"
        ],
        "correct_option": "D",
        "explanation": "Master-slave architecture prevents race-around toggling during sensor pulse counting."
      }
    ]
  },
  {
    "id": "MCQ-089",
    "title": "OS Access Matrix: Capability Lists vs Access Control Lists",
    "topic": "Operating Systems: Security & Access Control",
    "subtopic": "Protection Matrices and Capability Lists",
    "difficulty": "Medium",
    "source": "NIELIT 2020 Nov Scientist B: 88",
    "prompt": "In Operating System protection models based on the Access Matrix, what is the fundamental difference between an Access Control List (ACL) and a Capability List?",
    "options": [
      "A. ACLs are stored with the subjects (rows of matrix), while Capability Lists are stored with objects (columns of matrix)",
      "B. An ACL is object-centric (associating with each object a list of subjects and their rights), while a Capability List is subject-centric (associating with each subject a list of objects and permitted rights)",
      "C. ACLs apply only to network cards, while Capability Lists apply only to disk files",
      "D. Capability lists cannot be revoked"
    ],
    "correct_option": "B",
    "explanation": "An Access Matrix can be sliced in two ways: Column-wise decomposition yields Access Control Lists (ACLs, attached to objects, listing users and permissions). Row-wise decomposition yields Capability Lists (attached to subjects, representing unforgeable tokens granting rights to objects).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical operating system, how does an ACL on patient chart #404 differ from Dr. Lisa's Capability List?",
        "options": [
          "A. The ACL is attached to chart #404 listing authorized doctors; Dr. Lisa's Capability List is attached to Dr. Lisa listing all charts she can open",
          "B. Capabilities are stored in paper files",
          "C. ACLs are for nurses only, Capabilities are for doctors only",
          "D. There is no difference"
        ],
        "correct_option": "A",
        "explanation": "ACLs attach permissions to clinical objects; capability lists attach permission tokens to healthcare staff."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a bank vault security server, how does an ACL on the wire ledger differ from a teller's Capability token?",
        "options": [
          "A. The ledger ACL defines who can access the ledger; the teller's capability token defines all bank resources the teller can touch",
          "B. ACLs are forbidden in banking",
          "C. Capabilities cannot grant read access",
          "D. Capability tokens expire every second"
        ],
        "correct_option": "A",
        "explanation": "Object-centric ACLs protect specific files; subject-centric capabilities govern user authorization portfolios."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a multi-tenant cloud storage platform, how do bucket ACLs differ from tenant Capability tokens?",
        "options": [
          "A. ACLs are public while capabilities are encrypted",
          "B. Bucket ACLs specify which tenant accounts can read/write that bucket; capability tokens list all buckets a tenant is authorized to access",
          "C. Capabilities require biometric authentication",
          "D. Buckets cannot have ACLs"
        ],
        "correct_option": "B",
        "explanation": "ACLs decompose the access matrix by object column; capability lists decompose by subject row."
      }
    ]
  },
  {
    "id": "MCQ-090",
    "title": "Mandatory Access Control (MAC) & Multi-Level Security",
    "topic": "Operating Systems: Security & Access Control",
    "subtopic": "Bell-LaPadula and Multi-Level Security Rules",
    "difficulty": "Hard",
    "source": "NIELIT 2017 Oct Scientist B: 62",
    "prompt": "In Mandatory Access Control (MAC) under the Bell-LaPadula model, what do the 'Simple Security Property' and the '* -Property' (Star Property) mandate?",
    "options": [
      "A. Read-Up allowed, Write-Down allowed",
      "B. No Read-Up (a subject cannot read objects at a higher security level) and No Write-Down (a subject cannot write to objects at a lower security level)",
      "C. All users can read and write all objects freely",
      "D. Security levels change dynamically based on CPU load"
    ],
    "correct_option": "B",
    "explanation": "The Bell-LaPadula security model enforces confidentiality via two core rules: (1) Simple Security Property: 'No Read-Up' (a subject at clearance level L can only read objects at level <= L). (2) *-Property: 'No Write-Down' (a subject at clearance level L can only write objects at level >= L, preventing leakage of secret data to unclassified sinks).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a military trauma hospital handling classified soldier medical files, what does Bell-LaPadula MAC mandate?",
        "options": [
          "A. Civilian doctors cannot read Top-Secret soldier charts (No Read-Up), and Top-Secret surgeons cannot leak data into Unclassified logs (No Write-Down)",
          "B. Doctors can write to any lower level",
          "C. All medical records are published publicly",
          "D. Medical records have zero classifications"
        ],
        "correct_option": "A",
        "explanation": "No Read-Up protects confidentiality; No Write-Down prevents classified data leakage."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In central bank monetary policy systems, how does MAC prevent insider leaks before interest rate announcements?",
        "options": [
          "A. By enforcing No Read-Up for standard analysts, and No Write-Down for board governors to prevent copying embargoed rates to public folders",
          "B. By using unencrypted email",
          "C. By paying traders higher bonuses",
          "D. By disconnecting power to the building"
        ],
        "correct_option": "A",
        "explanation": "MAC rules strictly prohibit downward information flows from high-security clearances."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a defense contractor supply chain database enforcing MAC multi-level security:",
        "options": [
          "A. Customers can browse military schematics",
          "B. Uncleared vendors cannot read Secret aerospace specs (No Read-Up), and cleared engineers cannot copy Secret specs to public catalogs (No Write-Down)",
          "C. Prices are classified as Top Secret",
          "D. Suppliers choose their own clearance levels"
        ],
        "correct_option": "B",
        "explanation": "Multi-level security prevents unauthorized reading and unauthorized declassification."
      }
    ]
  },
  {
    "id": "MCQ-091",
    "title": "Software Engineering: Role-Based Actor Specification in Use Cases",
    "topic": "Software Engineering: Roles & Access Control",
    "subtopic": "UML Actor Roles and Access Boundaries",
    "difficulty": "Easy",
    "source": "NIELIT 2021 Dec Scientist B - Section B: 68",
    "prompt": "In UML software engineering and system modeling, what does an 'Actor' in a Use Case diagram represent?",
    "options": [
      "A. An internal database table containing employee records",
      "B. An external entity (human role, external hardware, or external system) that interacts with the system to achieve a specific goal",
      "C. A software developer writing backend code",
      "D. A physical CPU processor core"
    ],
    "correct_option": "B",
    "explanation": "In UML, an Actor is an external entity (outside the system boundary) that plays a role in interacting with the system. Actors can be human users (e.g. 'Customer', 'Admin'), external hardware devices (e.g. 'Barcode Scanner'), or third-party software systems (e.g. 'Payment Gateway').",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical EMR use-case diagram, which entity is modeled as an Actor outside the system boundary?",
        "options": [
          "A. Attending Physician who logs patient symptoms",
          "B. The SQL query compiler",
          "C. The Patient_ID integer column",
          "D. The hard drive controller"
        ],
        "correct_option": "A",
        "explanation": "Human roles interacting with medical software are modeled as external Actors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a mobile banking application use-case diagram, what is modeled as an Actor?",
        "options": [
          "A. Retail Account Holder and the external Visa Payment Network",
          "B. The primary key index block",
          "C. The database backup tape",
          "D. The balance calculation arithmetic logic unit"
        ],
        "correct_option": "A",
        "explanation": "Users and external financial networks interacting with the banking portal are UML Actors."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an online retail use-case model, which of the following is an Actor?",
        "options": [
          "A. The orders database table",
          "B. Guest Shopper and Third-Party Delivery Courier Service",
          "C. The web server power supply",
          "D. The CSS stylesheet"
        ],
        "correct_option": "B",
        "explanation": "External entities engaging with the marketplace platform represent use-case Actors."
      }
    ]
  },
  {
    "id": "MCQ-092",
    "title": "Database Check Constraints vs Triggers for Range Invariants",
    "topic": "Triggers & Active Databases",
    "subtopic": "Integrity Invariant Enforcement Techniques",
    "difficulty": "Medium",
    "source": "NIELIT 2016 DEC Scientist B: 54",
    "prompt": "Why is a table-level 'CHECK (Age >= 18)' constraint preferred over a 'BEFORE INSERT OR UPDATE' Trigger for validating simple attribute range boundaries?",
    "options": [
      "A. Triggers cannot evaluate mathematical comparison operators like >=",
      "B. CHECK constraints are declarative, compiled directly into table metadata, and execute with significantly lower overhead and no procedural context-switching",
      "C. Triggers only execute when the database restarts",
      "D. CHECK constraints can only be created on Sunday"
    ],
    "correct_option": "B",
    "explanation": "Declarative CHECK constraints are parsed and evaluated directly inside the tuple validation pipeline of the database storage engine. Procedural triggers require initializing a procedural language environment (PL/pgSQL), allocating trigger state, and performing context switches, resulting in higher execution overhead.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why should an EMR enforce 'CHECK (Heart_Rate > 0)' via a declarative constraint rather than a PL/pgSQL trigger?",
        "options": [
          "A. The declarative constraint avoids procedural runtime overhead and guarantees data integrity during high-volume telemetry ingestion",
          "B. Because heart rates are classified as text strings",
          "C. Because triggers cannot validate heart rates",
          "D. To prevent doctors from updating heart rates"
        ],
        "correct_option": "A",
        "explanation": "Declarative constraints validate vitals with minimal overhead during rapid sensor logging."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why is 'CHECK (Transfer_Amount > 0)' preferred over a banking trigger?",
        "options": [
          "A. It validates transfer amounts within the core storage engine without incurring procedural trigger overhead",
          "B. Because banking databases do not support PL/SQL",
          "C. To allow wire transfers without internet connections",
          "D. Because triggers cannot prevent negative transfers"
        ],
        "correct_option": "A",
        "explanation": "Declarative constraints enforce positive transaction amounts with optimal execution efficiency."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why use 'CHECK (Item_Quantity >= 1)' instead of an inventory trigger?",
        "options": [
          "A. Because triggers delete shopping carts",
          "B. High-frequency cart checkouts evaluate declarative constraints much faster than firing procedural trigger routines",
          "C. Because e-commerce only supports SQL-89",
          "D. To allow zero-item orders"
        ],
        "correct_option": "B",
        "explanation": "Declarative CHECK constraints maximize checkout throughput by avoiding procedural context switches."
      }
    ]
  },
  {
    "id": "MCQ-093",
    "title": "SQL Correlated Subquery Pairwise Evaluation",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Subquery Pairwise Comparison Invariants",
    "difficulty": "Medium",
    "source": "NIELIT 2022 Apr Scientist B: 39",
    "prompt": "Consider query: 'SELECT Emp_Name FROM Employees WHERE (Dept_ID, Salary) IN (SELECT Dept_ID, MAX(Salary) FROM Employees GROUP BY Dept_ID)'. What does this query return?",
    "options": [
      "A. It generates a syntax error because SQL does not support pairwise tuple comparison",
      "B. It retrieves the names of all employees who earn the maximum salary within their respective department",
      "C. It returns the employee with the lowest salary across the company",
      "D. It returns all employees in department 10 only"
    ],
    "correct_option": "B",
    "explanation": "SQL-92 supports row-constructor (pairwise) comparisons: (Dept_ID, Salary) IN (...). The subquery groups by Dept_ID and computes MAX(Salary) for each department. The outer query matches rows where the employee's department and salary match the department maximum pair.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "To find the highest-paid physician within each clinical hospital department using a single SQL query, the DBA writes:",
        "options": [
          "A. SELECT Doc_Name FROM Doctors WHERE (Dept_ID, Salary) IN (SELECT Dept_ID, MAX(Salary) FROM Doctors GROUP BY Dept_ID)",
          "B. SELECT Dept_ID FROM Doctors GROUP BY Doc_Name",
          "C. SELECT Doc_Name FROM Doctors WHERE Salary = 0",
          "D. TRUNCATE TABLE Doctors"
        ],
        "correct_option": "A",
        "explanation": "Pairwise tuple matching retrieves the exact doctor holding the maximum salary per department."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In loan management, to find the largest loan issued within each bank branch region:",
        "options": [
          "A. Match (Region_ID, Amount) IN (SELECT Region_ID, MAX(Amount) FROM Loans GROUP BY Region_ID)",
          "B. Delete loans below $1000",
          "C. Select count of loans",
          "D. Sum all loans per customer"
        ],
        "correct_option": "A",
        "explanation": "Row-value constructors cleanly match each loan against its region's maximum issued amount."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To find the top-selling product SKU within each product catalog category:",
        "options": [
          "A. Query WHERE Price = 0",
          "B. Query WHERE (Category_ID, Units_Sold) IN (SELECT Category_ID, MAX(Units_Sold) FROM Products GROUP BY Category_ID)",
          "C. Query ORDER BY Category_ID DESC",
          "D. Drop category index"
        ],
        "correct_option": "B",
        "explanation": "Pairwise comparisons select the specific top-selling SKU for every category."
      }
    ]
  },
  {
    "id": "MCQ-094",
    "title": "Network Access Control: Packet Filtering vs Stateful Inspection",
    "topic": "Computer Networks: Access Control & Security",
    "subtopic": "Firewall Access Control Lists and Packet Filtering",
    "difficulty": "Medium",
    "source": "NIELIT 2018 | Question: 82",
    "prompt": "In network security access control, what is a primary limitation of a stateless Packet-Filtering Router (stateless firewall) compared to a Stateful Inspection Firewall?",
    "options": [
      "A. Stateless routers cannot filter by IP address",
      "B. Stateless routers inspect packets in isolation and cannot track TCP connection states (e.g. SYN, ESTABLISHED), making them vulnerable to spoofed ACK packets",
      "C. Stateful firewalls only operate at the Physical Layer",
      "D. Stateless routers consume more CPU memory than stateful firewalls"
    ],
    "correct_option": "B",
    "explanation": "Stateless packet filters examine each packet header independently based on static rules (source/dest IP, port). They do not maintain a state table of active TCP sessions, meaning attackers can bypass filters by sending forged packets with the ACK bit set, pretending to belong to an established connection.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why must a hospital tele-surgery network use a stateful firewall rather than a simple stateless router?",
        "options": [
          "A. To track active tele-surgery connection sessions and block spoofed packets attempting to inject forged commands into medical robots",
          "B. Because stateless routers cannot transmit video",
          "C. To speed up fiber optic light speed",
          "D. To turn off hospital Wi-Fi at night"
        ],
        "correct_option": "A",
        "explanation": "Stateful firewalls verify incoming packets belong to legitimate established surgical sessions."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why do banks require stateful firewalls at the perimeter of automated clearing house (ACH) payment gateways?",
        "options": [
          "A. Stateful firewalls verify packets match verified three-way handshake TCP sessions, preventing forged payment packets",
          "B. Because stateless routers cannot handle decimal numbers",
          "C. To eliminate bank branches",
          "D. To allow anonymous bitcoin transfers"
        ],
        "correct_option": "A",
        "explanation": "Stateful inspection blocks malicious packets that attempt to bypass perimeter access controls."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why is stateful packet inspection required to protect payment card gateway servers from SYN flood attacks?",
        "options": [
          "A. Because stateless filters cannot accept credit card numbers",
          "B. Stateful firewalls monitor TCP handshake state transitions and drop rogue half-open connection attempts",
          "C. To automatically double customer checkout speed",
          "D. To disable SSL encryption"
        ],
        "correct_option": "B",
        "explanation": "Stateful session tracking protects payment infrastructure from connection-state exhaustion attacks."
      }
    ]
  },
  {
    "id": "MCQ-095",
    "title": "Edge-Triggered vs Level-Triggered Interrupt Handling in CPUs",
    "topic": "Computer Architecture: Interrupts & Execution",
    "subtopic": "Hardware Interrupt Triggering Modes",
    "difficulty": "Medium",
    "source": "NIELIT 2021 Dec Scientist B: 110",
    "prompt": "What critical hardware danger occurs if a peripheral device generates a Level-Triggered interrupt and the CPU's Interrupt Service Routine (ISR) fails to clear the interrupt flag on the device before re-enabling interrupts?",
    "options": [
      "A. The CPU immediately encounters an infinite interrupt loop, repeatedly re-entering the ISR as soon as interrupts are enabled",
      "B. The computer's hard drive is wiped",
      "C. The interrupt line permanently burns out physically",
      "D. The CPU switches to 16-bit real mode"
    ],
    "correct_option": "A",
    "explanation": "With level-triggered interrupts, the interrupt line remains asserted (e.g. held LOW or HIGH) as long as the device has a pending request. If the ISR exits without commanding the peripheral to de-assert the line, the CPU samples the active level again and immediately re-triggers the ISR infinitely.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If an infusion pump controller asserts a level-triggered interrupt on low battery and the firmware ISR fails to acknowledge it, what happens?",
        "options": [
          "A. The battery immediately recharges to 100%",
          "B. The controller loops infinitely re-entering the battery ISR, freezing pump motor controls",
          "C. The LCD screen displays random characters",
          "D. The infusion pump explodes"
        ],
        "correct_option": "B",
        "explanation": "Failure to de-assert level-triggered lines causes infinite ISR re-triggering."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In an ATM keypad controller, if a keypress asserts a level-triggered interrupt and the software fails to acknowledge the key register:",
        "options": [
          "A. The ATM dispenses all its cash",
          "B. The keypad converts to touchscreen",
          "C. The ATM CPU locks up re-executing the keypress ISR infinitely",
          "D. The user PIN is sent to the internet"
        ],
        "correct_option": "C",
        "explanation": "Level-triggered lines must be actively cleared by the handler to prevent interrupt lockups."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an automated warehouse sorting arm controller, what happens if a level-triggered optical sensor interrupt is not cleared by firmware?",
        "options": [
          "A. The barcode laser turns green",
          "B. Packages are sorted in reverse",
          "C. The arm moves twice as fast",
          "D. The microcontroller becomes trapped in a continuous interrupt loop, stalling the conveyor arm"
        ],
        "correct_option": "D",
        "explanation": "Unacknowledged level signals cause the processor to endlessly re-invoke the interrupt handler."
      }
    ]
  },
  {
    "id": "MCQ-096",
    "title": "Database Cursor Lifecycle: Declare, Open, Fetch, Close",
    "topic": "Triggers & Active Databases",
    "subtopic": "Procedural Cursors and Iterative Processing",
    "difficulty": "Easy",
    "source": "NIELIT 2020 Nov Assistant A: 45",
    "prompt": "In relational database procedural programming (PL/SQL), what is the correct chronological sequence of operations in the lifecycle of an explicit database cursor?",
    "options": [
      "A. OPEN -> DECLARE -> FETCH -> CLOSE",
      "B. DECLARE -> OPEN -> FETCH -> CLOSE",
      "C. FETCH -> OPEN -> DECLARE -> CLOSE",
      "D. DECLARE -> FETCH -> OPEN -> CLOSE"
    ],
    "correct_option": "B",
    "explanation": "The standard lifecycle of an explicit SQL cursor is: (1) DECLARE (defines cursor name and associated SELECT query), (2) OPEN (executes query, allocates memory, positions pointer before first row), (3) FETCH (retrieves current row into variables and advances pointer), (4) CLOSE (releases cursor memory and locks).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When an EMR batch process iterates through active ICU patients to calculate daily fluid balance, what is the cursor execution order?",
        "options": [
          "A. Declare cursor query -> Open cursor (allocate buffers) -> Fetch patient rows in loop -> Close cursor (free memory)",
          "B. Close -> Open -> Fetch -> Declare",
          "C. Fetch -> Open -> Close -> Declare",
          "D. Open -> Fetch -> Close -> Declare"
        ],
        "correct_option": "A",
        "explanation": "DECLARE -> OPEN -> FETCH -> CLOSE is the invariant lifecycle of relational cursors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In end-of-day bank interest accrual processing across millions of savings accounts, what is the cursor sequence?",
        "options": [
          "A. DECLARE -> OPEN -> FETCH -> CLOSE",
          "B. FETCH -> CLOSE -> DECLARE -> OPEN",
          "C. DECLARE -> CLOSE -> OPEN -> FETCH",
          "D. OPEN -> FETCH -> DECLARE -> CLOSE"
        ],
        "correct_option": "A",
        "explanation": "Cursors must be declared, opened to initialize active sets, fetched in loops, and closed to release locks."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When a monthly subscription engine iterates through customer profiles to generate recurring invoices, the cursor steps are:",
        "options": [
          "A. FETCH -> DECLARE -> OPEN -> CLOSE",
          "B. DECLARE -> OPEN -> FETCH -> CLOSE",
          "C. OPEN -> CLOSE -> DECLARE -> FETCH",
          "D. DECLARE -> OPEN -> CLOSE -> FETCH"
        ],
        "correct_option": "B",
        "explanation": "Explicit cursors must always follow the DECLARE-OPEN-FETCH-CLOSE lifecycle."
      }
    ]
  },
  {
    "id": "MCQ-097",
    "title": "Schema Level Assertions in Relational Standards",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Schema Assertions vs Procedural Logic",
    "difficulty": "Medium",
    "source": "NIELIT 2019 Scientist B: 18",
    "prompt": "Under the SQL-92 standard, what SQL statement is used to define an integrity constraint that spans across multiple tables and must be satisfied by every database state?",
    "options": [
      "A. CREATE ASSERTION <name> CHECK (<condition>);",
      "B. ALTER TABLE <name> ADD CONSTRAINT MULTI;",
      "C. CREATE MULTI_CHECK <condition>;",
      "D. CREATE TRIGGER <name> ON ALL TABLES;"
    ],
    "correct_option": "A",
    "explanation": "In SQL-92, schema-level multi-table invariants are declared using: CREATE ASSERTION <assertion_name> CHECK (<predicate>). Any DML operation that causes the predicate to evaluate to FALSE is aborted and rolled back by the DBMS.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "To enforce a global hospital rule that total nurses on duty across all wards must exceed total admitted ICU patients, what SQL standard command is defined?",
        "options": [
          "A. ALTER TABLE Nurses ADD CONSTRAINT nurse_check;",
          "B. CREATE ASSERTION nurse_to_patient_ratio CHECK ((SELECT COUNT(*) FROM Nurses WHERE Status='OnDuty') > (SELECT COUNT(*) FROM Patients WHERE Ward='ICU'));",
          "C. DROP TABLE Patients;",
          "D. CREATE VIEW Hospital_Rules AS SELECT * FROM Nurses;"
        ],
        "correct_option": "B",
        "explanation": "CREATE ASSERTION enforces multi-table aggregate invariants across hospital staff and patients."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "To mandate that total loans issued across all branches never exceed 80% of total bank deposits across all accounts, the SQL standard statement is:",
        "options": [
          "A. CREATE TABLE Reserve(ratio INT);",
          "B. ALTER DATABASE SET LOANS = 0;",
          "C. CREATE ASSERTION reserve_ratio CHECK ((SELECT SUM(Loan_Amount) FROM Loans) <= 0.8 * (SELECT SUM(Balance) FROM Deposits));",
          "D. GRANT ALL PRIVILEGES ON Deposits TO Loans;"
        ],
        "correct_option": "C",
        "explanation": "Schema-level assertions enforce global cross-table capital reserve ratios."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To ensure that total gift card credit issued across all accounts never exceeds the escrow account balance:",
        "options": [
          "A. CREATE TRIGGER ON Escrow DELETE;",
          "B. ALTER TABLE Gift_Cards DROP COLUMN Card_Balance;",
          "C. SELECT * FROM Gift_Cards CROSS JOIN Escrow;",
          "D. CREATE ASSERTION escrow_check CHECK ((SELECT SUM(Card_Balance) FROM Gift_Cards) <= (SELECT Escrow_Balance FROM Escrow));"
        ],
        "correct_option": "D",
        "explanation": "CREATE ASSERTION enforces global balance invariants across Gift_Cards and Escrow tables."
      }
    ]
  },
  {
    "id": "MCQ-098",
    "title": "Relational Domain Constraints and Data Typing",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Domain Constraints and Value Sets",
    "difficulty": "Easy",
    "source": "NIELIT 2017 July Scientist B: 66",
    "prompt": "In relational database theory, what does a 'Domain Constraint' define for an attribute?",
    "options": [
      "A. The list of users permitted to query the column",
      "B. The set of all permissible atomic values (data type, size, format, and allowable value range) that the attribute can take",
      "C. The foreign key parent relation name",
      "D. The disk sector address where the attribute is physically stored"
    ],
    "correct_option": "B",
    "explanation": "A domain constraint specifies the set of valid atomic values permitted for an attribute. It encompasses the underlying primitive data type (e.g. INT, VARCHAR), length limits, nullability, and custom user-defined domain checks (e.g. CREATE DOMAIN Gender AS CHAR(1) CHECK (VALUE IN ('M', 'F', 'O'))).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an EMR, defining a custom domain 'Blood_Type AS VARCHAR(3) CHECK (VALUE IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))' is an example of:",
        "options": [
          "A. A Domain Constraint restricting attribute values to valid medical blood groups",
          "B. A database deadlock prevention policy",
          "C. An encrypted hash algorithm",
          "D. An operating system kernel call"
        ],
        "correct_option": "A",
        "explanation": "Domain constraints restrict attribute values to medically valid blood groups."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In banking schemas, defining 'Currency_Code AS CHAR(3) CHECK (VALUE IN ('USD', 'EUR', 'GBP', 'JPY'))' represents:",
        "options": [
          "A. A Domain Constraint enforcing ISO currency code validity",
          "B. A secondary B+ tree index",
          "C. A database backup schedule",
          "D. An interest rate calculation formula"
        ],
        "correct_option": "A",
        "explanation": "Domain constraints guarantee that only recognized currency codes are stored."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In a marketplace catalog, defining 'Rating AS NUMERIC(2,1) CHECK (VALUE BETWEEN 1.0 AND 5.0)' is:",
        "options": [
          "A. A shopping cart checkout trigger",
          "B. A Domain Constraint establishing valid customer review score ranges",
          "C. A database user password",
          "D. An external web API endpoint"
        ],
        "correct_option": "B",
        "explanation": "Domain constraints validate that review ratings stay within bounded scalar ranges."
      }
    ]
  },
  {
    "id": "MCQ-099",
    "title": "Concurrency Serializability Graph Cycle Detection",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Precedence Graphs and Cycle Detection",
    "difficulty": "Hard",
    "source": "NIELIT 2018 | Question: 50",
    "prompt": "Given schedule S: r1(X); r2(Y); w1(Y); w2(X); commit1; commit2. Constructing the precedence graph for S produces:",
    "options": [
      "A. A cycle between T1 and T2 (T1 -> T2 and T2 -> T1), proving the schedule is NOT conflict serializable",
      "B. An acyclic graph with topological order T1, T2",
      "C. A graph with no edges",
      "D. A tree structure with T1 as root"
    ],
    "correct_option": "A",
    "explanation": "Let's trace conflicting operations: r2(Y) precedes w1(Y) on Y -> directed edge T2 -> T1. r1(X) precedes w2(X) on X -> directed edge T1 -> T2. The graph contains a directed cycle T1 ⇄ T2, proving S is not conflict serializable.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Doctor T1 reads patient meds (X) and writes vitals (Y). Doctor T2 reads vitals (Y) and writes meds (X). Why is this concurrent charting schedule unsafe?",
        "options": [
          "A. Because doctors cannot edit charts concurrently",
          "B. It produces a directed cycle T1 -> T2 and T2 -> T1 in the precedence graph, creating an un-serializable conflict schedule",
          "C. Because X and Y are invalid medical variables",
          "D. Because patient charts are stored in read-only memory"
        ],
        "correct_option": "B",
        "explanation": "Bidirectional conflict edges form cycles that destroy conflict serializability in medical charts."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Transfer T1 reads Account A and writes Account B. Transfer T2 reads Account B and writes Account A. Why is this schedule rejected by a serializable engine?",
        "options": [
          "A. Because transfers must be executed on weekdays only",
          "B. Because Account A and B have different owners",
          "C. The conflicting operations form a directed cycle between T1 and T2, violating conflict serializability",
          "D. Because transactions require three accounts"
        ],
        "correct_option": "C",
        "explanation": "Dependency cycles indicate non-serializable interleaving that can corrupt balances."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Order T1 reads stock (X) and updates promo (Y). Order T2 reads promo (Y) and updates stock (X). What does precedence graph analysis show?",
        "options": [
          "A. The schedule is completely safe",
          "B. Both orders should be discounted by 100%",
          "C. Precedence graphs do not apply to inventory",
          "D. A directed cycle T1 <-> T2 exists, proving the execution is not conflict serializable"
        ],
        "correct_option": "D",
        "explanation": "Acyclic graphs are mandatory for conflict serializability; cycles prove non-serializability."
      }
    ]
  },
  {
    "id": "MCQ-100",
    "title": "Write-Ahead Logging WAL Protocol Rules",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "WAL Protocol Flushing Rules",
    "difficulty": "Medium",
    "source": "NIELIT 2021 Dec Scientist B: 118",
    "prompt": "Under the Write-Ahead Logging (WAL) protocol, which rule MUST be enforced by the database buffer manager before a modified dirty data page can be written to disk?",
    "options": [
      "A. All active transactions must commit first",
      "B. The log record corresponding to the update (with its undo information) must be flushed to non-volatile disk BEFORE the dirty data page itself is written to disk",
      "C. The database index must be dropped and recreated",
      "D. The user session must be disconnected"
    ],
    "correct_option": "B",
    "explanation": "The foundational WAL rule states: The log record describing a change to a database object must be flushed to stable storage before the database object containing that change is allowed to be flushed to disk. This guarantees that if a crash occurs immediately after the page flush, undo records exist to roll back uncommitted changes.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Before saving an updated patient chart page to physical SSD storage, what does the EMR storage engine flush first?",
        "options": [
          "A. The Write-Ahead Log undo record for that patient chart update must be written to stable storage first",
          "B. The doctor's electronic signature to cloud backup",
          "C. The hospital billing invoice",
          "D. The entire database to tape"
        ],
        "correct_option": "A",
        "explanation": "WAL mandates log records flush before dirty clinical data pages touch persistent disk."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why must a banking database write ledger log records to disk before writing the modified account balance pages?",
        "options": [
          "A. To ensure that if a power outage occurs while writing the account page, the log contains the necessary undo information to reverse the partial write upon reboot",
          "B. Because disk controllers cannot write numbers directly",
          "C. Because account pages are read-only",
          "D. To slow down transaction throughput"
        ],
        "correct_option": "A",
        "explanation": "WAL ensures undo information is guaranteed to be on disk before dirty data is overwritten."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce database recovery, what does WAL require before persisting an updated inventory table block to SSD?",
        "options": [
          "A. Emailing the customer a receipt",
          "B. Writing the inventory log record containing undo/redo bytes to stable storage first",
          "C. Checking the warehouse security cameras",
          "D. Clearing all customer browser cookies"
        ],
        "correct_option": "B",
        "explanation": "The WAL invariant requires log flushing strictly ahead of dirty data page eviction."
      }
    ]
  },
  {
    "id": "MCQ-101",
    "title": "Event-Condition-Action (ECA) Rule Model & Triggers",
    "topic": "Triggers & Active Databases",
    "subtopic": "ECA Model and Active Database Concepts",
    "difficulty": "Medium",
    "source": "UGC NET CSE June 2013 | Part 3 | Question: 47",
    "prompt": "In active database architectures, which structural model pairs with 'Triggers' to govern automatic reactive rule processing?",
    "options": [
      "A. Private key encryption",
      "B. Event-Condition-Action (ECA) model",
      "C. Domain integrity constraints",
      "D. Relational calculus division"
    ],
    "correct_option": "B",
    "explanation": "In active databases, triggers are the primary implementation of the Event-Condition-Action (ECA) model: an Event (INSERT/UPDATE/DELETE) activates the rule, a Condition (logical query predicate) is evaluated, and if TRUE, an Action (procedural SQL block) is automatically executed.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital monitoring database, when an EKG telemetry update triggers an automated defibrillator alert, what architectural rule model is executing?",
        "options": [
          "A. Event-Condition-Action (ECA) model (Event: EKG update -> Condition: heart rate < 40 -> Action: trigger alarm)",
          "B. B-tree index balancing",
          "C. Passive file storage",
          "D. Data warehouse cube projection"
        ],
        "correct_option": "A",
        "explanation": "Active EMR telemetry alerts implement the foundational Event-Condition-Action model."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In automated anti-money laundering (AML), when a deposit exceeding $10,000 triggers an automated compliance freeze, what model is applied?",
        "options": [
          "A. Event-Condition-Action (ECA) trigger model",
          "B. Cryptographic RSA key exchange",
          "C. Two-phase locking",
          "D. Discretionary access matrix"
        ],
        "correct_option": "A",
        "explanation": "AML compliance rules execute under the active database Event-Condition-Action framework."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When an inventory update detects stock < 10 and automatically places a supplier restocking order, what rule model is in effect?",
        "options": [
          "A. A domain constraint check",
          "B. The Event-Condition-Action (ECA) trigger architecture",
          "C. An unindexed hash bucket",
          "D. A manual user prompt"
        ],
        "correct_option": "B",
        "explanation": "Automated inventory re-ordering is an implementation of the ECA active rule model."
      }
    ]
  },
  {
    "id": "MCQ-102",
    "title": "SQL Schema Assertions: CREATE ASSERTION Invariants",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "Schema-Level Assertions vs Single Table Checks",
    "difficulty": "Hard",
    "source": "UGC NET CSE June 2015 | Part 2 | Question: 16",
    "prompt": "An Assertion is a predicate expressing a condition we wish the database to always satisfy. What is the correct SQL standard syntax for declaring an Assertion?",
    "options": [
      "A. CREATE ASSERTION <name> CHECK (<predicate>);",
      "B. ALTER TABLE <name> ADD ASSERTION (<predicate>);",
      "C. CREATE CONSTRAINT <name> ON DATABASE (<predicate>);",
      "D. CREATE TRIGGER <name> AS ASSERTION (<predicate>);"
    ],
    "correct_option": "A",
    "explanation": "As defined in the SQL-92 standard: 'CREATE ASSERTION <assertion_name> CHECK (<predicate>);' creates a schema-level declarative constraint spanning one or more tables that must evaluate to TRUE or UNKNOWN for all valid database states.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "To enforce a clinical rule that the sum of admitted ICU patients across all wards cannot exceed ICU nurse capacity, how is a schema assertion declared?",
        "options": [
          "A. ALTER TABLE Patients ADD ASSERTION icu_check;",
          "B. CREATE ASSERTION icu_capacity_check CHECK ((SELECT COUNT(*) FROM Patients WHERE Ward='ICU') <= (SELECT COUNT(*)*2 FROM Nurses WHERE Ward='ICU'));",
          "C. DROP TABLE Nurses;",
          "D. CREATE TRIGGER icu_capacity_check ON Patients AFTER DELETE;"
        ],
        "correct_option": "B",
        "explanation": "CREATE ASSERTION defines cross-table aggregate constraints in SQL standards."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "How does a banking DBA declare an assertion that total customer credit lines cannot exceed total bank capitalization?",
        "options": [
          "A. ALTER TABLE Customers SET LIMIT = CAPITAL;",
          "B. CREATE VIEW Credit_Cap AS SELECT 1;",
          "C. CREATE ASSERTION credit_cap_check CHECK ((SELECT SUM(Credit_Limit) FROM Customers) <= (SELECT Total_Capital FROM Bank_Capital));",
          "D. GRANT ASSERTION TO Admin;"
        ],
        "correct_option": "C",
        "explanation": "Schema-level assertions guarantee global capital adequacy constraints across tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To ensure that total gift card balances across all users never exceed the cash escrow balance, the standard SQL declaration is:",
        "options": [
          "A. ALTER TABLE Gift_Cards SET BALANCE = 0;",
          "B. CREATE DOMAIN Escrow AS INT;",
          "C. LOCK TABLE Gift_Cards IN EXCLUSIVE MODE;",
          "D. CREATE ASSERTION escrow_invariant CHECK ((SELECT SUM(Balance) FROM Gift_Cards) <= (SELECT Escrow_Amount FROM Escrow));"
        ],
        "correct_option": "D",
        "explanation": "CREATE ASSERTION enforces global financial invariants across distinct database tables."
      }
    ]
  },
  {
    "id": "MCQ-103",
    "title": "SQL View Updatability & WITH CHECK OPTION Invariants",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "View Updatability and WITH CHECK OPTION",
    "difficulty": "Medium",
    "source": "UGC NET CSE Dec 2015 | Part 2 | Question: 18",
    "prompt": "What is the effect of appending 'WITH CHECK OPTION' to a CREATE VIEW statement in SQL?",
    "options": [
      "A. It converts the view into an in-memory materialized snapshot",
      "B. It prevents any INSERT or UPDATE through the view that would produce rows that do not satisfy the view's WHERE clause",
      "C. It disables all foreign key checks on the underlying base tables",
      "D. It grants SELECT access to all public users"
    ],
    "correct_option": "B",
    "explanation": "WITH CHECK OPTION ensures that any INSERT or UPDATE performed through the view must satisfy the view's WHERE condition. If an update would cause a row to disappear from the view (or an insert would not be visible in the view), the database engine rejects the modification.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A view 'Adult_Patients' selects patients WHERE Age >= 18 WITH CHECK OPTION. What happens if a doctor tries to insert a patient with Age = 12 through this view?",
        "options": [
          "A. The insert is rejected immediately because Age = 12 does not satisfy the view's WHERE condition",
          "B. The view is deleted",
          "C. The patient is inserted and Age is forced to 18",
          "D. The patient record is saved in a quarantine table"
        ],
        "correct_option": "A",
        "explanation": "WITH CHECK OPTION prevents inserting pediatric patients through an adult view."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "A view 'Active_Accounts' filters WHERE Status = 'Active' WITH CHECK OPTION. A teller updates an account through the view setting Status = 'Suspended'. What occurs?",
        "options": [
          "A. The update is rejected by the DBMS because the resulting row would no longer satisfy the view predicate",
          "B. The teller's account is locked",
          "C. The update succeeds silently",
          "D. The account is deleted from the bank"
        ],
        "correct_option": "A",
        "explanation": "WITH CHECK OPTION blocks updates that cause rows to leave the view's defined domain."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "A view 'In_Stock_Products' selects items WHERE Stock_Qty > 0 WITH CHECK OPTION. An update sets Stock_Qty = 0 through the view. How does the database respond?",
        "options": [
          "A. Stock becomes negative",
          "B. The update fails with a CHECK OPTION violation",
          "C. The product is shipped automatically",
          "D. The view is converted to a base table"
        ],
        "correct_option": "B",
        "explanation": "WITH CHECK OPTION preserves view invariant membership under all DML operations."
      }
    ]
  },
  {
    "id": "MCQ-104",
    "title": "Referential Integrity: Recursive Foreign Key Deletions",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Foreign Key Deletion Traversal and Invariants",
    "difficulty": "Hard",
    "source": "UGC NET CSE Dec 2012 | Part 3 | Question: 70",
    "prompt": "In a database enforcing referential integrity, if parent table P is referenced by child table C with ON DELETE RESTRICT, what occurs when a user executes 'DELETE FROM P WHERE P_ID = 10' when matching rows exist in C?",
    "options": [
      "A. Matching child rows in C are automatically deleted",
      "B. The deletion of the parent row in P is immediately prohibited and rolled back by the DBMS",
      "C. Matching rows in C have their foreign keys set to NULL",
      "D. The parent row is deleted and child rows become orphan tuples"
    ],
    "correct_option": "B",
    "explanation": "ON DELETE RESTRICT (and the equivalent NO ACTION) prevents the deletion of a referenced primary key tuple as long as any referencing child tuples exist in related tables. The operation is blocked and an integrity violation error is raised.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In hospital records with ON DELETE RESTRICT between Patients and Prescriptions, what happens when someone attempts to delete a patient who has active prescriptions?",
        "options": [
          "A. The deletion is blocked, protecting active prescription records from being orphaned",
          "B. The doctor is notified by email",
          "C. All active prescriptions are burned",
          "D. Prescriptions are reassigned to patient 0"
        ],
        "correct_option": "A",
        "explanation": "RESTRICT prevents deleting patients who have dependent active prescriptions."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "With ON DELETE RESTRICT between Accounts and Transactions, what occurs if a clerk attempts to delete an account having recorded transactions?",
        "options": [
          "A. The transaction engine halts and rejects the account deletion to preserve audit integrity",
          "B. Account balance is converted to zero",
          "C. The database creates a duplicate account",
          "D. Transactions are wiped from the ledger"
        ],
        "correct_option": "A",
        "explanation": "RESTRICT enforces historical auditability by preventing parent account deletion."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an online catalog with ON DELETE RESTRICT between Categories and Products, deleting a category that contains active products results in:",
        "options": [
          "A. Deletion of all products in that category",
          "B. Immediate rejection of the category deletion by the relational engine",
          "C. Free products for all customers",
          "D. Creation of an unindexed category"
        ],
        "correct_option": "B",
        "explanation": "RESTRICT prohibits category deletion while referencing product rows remain."
      }
    ]
  },
  {
    "id": "MCQ-105",
    "title": "Database Security: Discretionary Access Control (DAC) via GRANT",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Discretionary Access and Privilege Propagation",
    "difficulty": "Medium",
    "source": "UGC NET CSE June 2014 | Part 2 | Question: 48",
    "prompt": "When user A executes 'GRANT SELECT ON Table1 TO UserB WITH GRANT OPTION', what capability has user A bestowed upon user B?",
    "options": [
      "A. User B can only read Table1, but cannot share the permission with others",
      "B. User B can read Table1 AND possesses the authority to grant SELECT privileges on Table1 to other database users",
      "C. User B becomes the database superuser",
      "D. User B can drop Table1"
    ],
    "correct_option": "B",
    "explanation": "WITH GRANT OPTION confers not only the specified access privilege (SELECT) to the grantee (User B), but also the authority to grant that privilege to third-party users, forming an authorization delegation tree.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When Chief Medical Officer Dr. A grants chart viewing rights to Head Nurse B 'WITH GRANT OPTION', what can Nurse B do?",
        "options": [
          "A. View patient charts and grant chart viewing rights to shift nurses under her supervision",
          "B. Prescribe narcotics without a medical license",
          "C. Delete hospital billing records",
          "D. Shut down the hospital data center"
        ],
        "correct_option": "A",
        "explanation": "WITH GRANT OPTION delegates administrative granting power for clinical chart access."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If an investment bank auditor receives SELECT on the Wire_Ledger 'WITH GRANT OPTION', the auditor can:",
        "options": [
          "A. Read the ledger and delegate read permissions to external auditing associates",
          "B. Alter ledger debit entries",
          "C. Revoke DBA master passwords",
          "D. Wire money to personal accounts"
        ],
        "correct_option": "A",
        "explanation": "WITH GRANT OPTION enables privilege propagation to subordinate auditors."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When a marketplace admin grants UPDATE on Products to Vendor_Manager 'WITH GRANT OPTION':",
        "options": [
          "A. The Vendor Manager can view customer credit card numbers",
          "B. The Vendor Manager can update products and grant product update privileges to sub-vendors",
          "C. The database drops all indexes",
          "D. Products are automatically discounted"
        ],
        "correct_option": "B",
        "explanation": "Grant option allows authorized managers to cascade permissions to vendor team members."
      }
    ]
  },
  {
    "id": "MCQ-106",
    "title": "Cascade Option on REVOKE: Recursive Permission Withdrawal",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "REVOKE CASCADE vs RESTRICT Invariants",
    "difficulty": "Hard",
    "source": "UGC NET CSE July 2016 | Part 2 | Question: 16",
    "prompt": "User A grants privilege P to User B with grant option. User B grants P to User C. If User A executes 'REVOKE P FROM UserB CASCADE', what is the resulting authorization state of User C?",
    "options": [
      "A. User C retains privilege P because grants are immutable once bestowed",
      "B. Privilege P is recursively revoked from User C (and any users granted P by C) along the authorization dependency tree",
      "C. User C is promoted to take User B's place",
      "D. The revoke fails with a deadlock error"
    ],
    "correct_option": "B",
    "explanation": "Under SQL access control rules: REVOKE ... CASCADE traverses the authorization dependency graph. When User B's privilege is revoked, any privileges that User B granted to others (User C) that have no other independent granting paths are recursively revoked as well.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Dr. A grants chart access to Resident B with grant option, who grants it to Intern C. When Dr. A revokes B's access CASCADE upon B's rotation ending:",
        "options": [
          "A. Intern C's access is also automatically revoked, maintaining strict patient data privacy",
          "B. Intern C becomes chief resident",
          "C. Intern C keeps chart access indefinitely",
          "D. Patient records are locked forever"
        ],
        "correct_option": "A",
        "explanation": "REVOKE CASCADE cleans up delegated permissions down the clinical supervision chain."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Bank Officer A grants wire authorization to Assistant B with grant option, who delegates to Clerk C. If A revokes B's privilege CASCADE:",
        "options": [
          "A. Clerk C's wire authorization is automatically revoked by the database engine",
          "B. The bank is audited by the SEC",
          "C. Assistant B's account is deleted",
          "D. Clerk C can still wire money"
        ],
        "correct_option": "A",
        "explanation": "Cascading revokes eliminate orphaned financial transfer permissions down the delegation tree."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If Manager A grants pricing rights to Lead B with grant option, who delegates to Specialist C: executing REVOKE CASCADE on B results in:",
        "options": [
          "A. Specialist C gaining full admin access",
          "B. Automatic revocation of pricing privileges from both B and Specialist C",
          "C. Product prices becoming free",
          "D. The products table being dropped"
        ],
        "correct_option": "B",
        "explanation": "Cascading revokes withdraw permissions recursively along the authorization graph."
      }
    ]
  },
  {
    "id": "MCQ-107",
    "title": "SQL Foreign Key Definition Syntax & Referential Actions",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Declarative Foreign Key DDL Invariants",
    "difficulty": "Medium",
    "source": "UGC NET CSE Oct 2020 | Part 2 | Question: 96",
    "prompt": "In SQL DDL, which clause correctly defines a foreign key in table Department(Dept_ID, Mgr_ID) referencing table Employee(Emp_ID) with automatic deletion propagation?",
    "options": [
      "A. FOREIGN KEY (Mgr_ID) REFERENCES Employee(Emp_ID) ON DELETE CASCADE",
      "B. FOREIGN KEY (Mgr_ID) EQUALS Employee(Emp_ID) CASCADE",
      "C. CONSTRAINT Mgr_ID MATCHES Employee(Emp_ID)",
      "D. LINK Mgr_ID TO Employee(Emp_ID) WITH DELETE"
    ],
    "correct_option": "A",
    "explanation": "The standard ANSI SQL syntax for declaring a foreign key with cascading deletes is: FOREIGN KEY (child_column) REFERENCES ParentTable(parent_column) ON DELETE CASCADE.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "To declare that deleting a Physician automatically cascades to delete their Ward_Assignments records, the DBA specifies:",
        "options": [
          "A. CHECK (Physician_ID IN Physicians)",
          "B. FOREIGN KEY (Physician_ID) REFERENCES Physicians(Doc_ID) ON DELETE CASCADE",
          "C. TRIGGER ON DELETE PHYSICIANS",
          "D. ALTER DATABASE DROP PHYSICIAN"
        ],
        "correct_option": "B",
        "explanation": "FOREIGN KEY ... REFERENCES ... ON DELETE CASCADE is standard ANSI SQL DDL syntax."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In account management schemas, what SQL DDL clause links Account_Cards to Accounts with cascade delete?",
        "options": [
          "A. CONNECT Account_No WITH Accounts",
          "B. SET FOREIGN KEY ON Accounts",
          "C. FOREIGN KEY (Account_No) REFERENCES Accounts(Account_No) ON DELETE CASCADE",
          "D. MERGE Account_No INTO Accounts"
        ],
        "correct_option": "C",
        "explanation": "Standard declarative DDL syntax links child card records to master accounts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To link Order_Items to master Orders table with automatic cascade cleanup on canceled orders:",
        "options": [
          "A. JOIN ON Order_ID CASCADE",
          "B. PRIMARY KEY Order_ID REFERENCES Orders",
          "C. DROP Order_ID ON CASCADE",
          "D. FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) ON DELETE CASCADE"
        ],
        "correct_option": "D",
        "explanation": "Foreign key cascading syntax links order lines to header records."
      }
    ]
  },
  {
    "id": "MCQ-108",
    "title": "ON DELETE SET NULL vs ON DELETE CASCADE Semantics",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Action Comparisons",
    "difficulty": "Medium",
    "source": "UGC NET CSE Oct 2020 | Part 2 | Question: 97",
    "prompt": "What is the key functional difference between foreign key referential actions 'ON DELETE SET NULL' and 'ON DELETE CASCADE'?",
    "options": [
      "A. SET NULL deletes child rows, whereas CASCADE retains child rows with NULL values",
      "B. CASCADE deletes matching child rows when the parent row is deleted, whereas SET NULL retains matching child rows and updates their foreign key columns to NULL",
      "C. SET NULL can only be used on primary keys",
      "D. CASCADE is only supported in SQLite"
    ],
    "correct_option": "B",
    "explanation": "ON DELETE CASCADE physically deletes all referencing child rows when the parent is deleted. ON DELETE SET NULL retains the child rows in the database, but updates their referencing foreign key attributes to NULL (requiring the child column to be nullable).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When a consulting specialist is removed from a hospital staff directory, why is ON DELETE SET NULL preferred on Patient_Records(Consultant_ID) over ON DELETE CASCADE?",
        "options": [
          "A. Because ON DELETE CASCADE would dangerously delete the patient records, whereas SET NULL preserves the patient records while blanking the consultant reference",
          "B. Because patient records have no primary keys",
          "C. Because consultants cannot be deleted",
          "D. Because SET NULL converts patient names to numbers"
        ],
        "correct_option": "A",
        "explanation": "SET NULL prevents accidental deletion of clinical patient records when secondary consultants leave."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When a branch manager leaves a bank, why should Branch(Manager_ID) use ON DELETE SET NULL rather than ON DELETE CASCADE?",
        "options": [
          "A. To prevent deleting the physical bank branch and its accounts when a manager resigns",
          "B. Because banks cannot have null managers",
          "C. To double bank profits",
          "D. Because managers are primary keys"
        ],
        "correct_option": "A",
        "explanation": "SET NULL leaves the physical branch operational with an unassigned manager slot."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When an affiliate marketer account is deleted, why does Orders(Affiliate_ID) use ON DELETE SET NULL?",
        "options": [
          "A. It refunds all customer orders",
          "B. It preserves customer order records and purchase history while nullifying the affiliate commission reference",
          "C. It cancels all shipment deliveries",
          "D. It shuts down the web server"
        ],
        "correct_option": "B",
        "explanation": "SET NULL maintains transactional order history when non-critical metadata owners are deleted."
      }
    ]
  },
  {
    "id": "MCQ-109",
    "title": "Composite Foreign Key Referential Matching",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Composite Foreign Key Matching Semantics",
    "difficulty": "Hard",
    "source": "UGC NET CSE Oct 2020 | Part 2 | Question: 98",
    "prompt": "In relational database schemas with composite keys, when a child table declares a composite foreign key (A, B) referencing parent table (P_A, P_B):",
    "options": [
      "A. The child row satisfies referential integrity if A matches any P_A regardless of B",
      "B. The combination of values (A, B) in the child tuple must exactly match the combined values (P_A, P_B) of a single tuple in the parent table (or both be NULL under MATCH FULL)",
      "C. Attribute A must be identical to attribute B in the child table",
      "D. Parent table must be unindexed"
    ],
    "correct_option": "B",
    "explanation": "Composite foreign keys reference multi-attribute candidate keys. Referential integrity requires that the entire tuple of foreign key values (A, B) must find an exact pairwise match in a single parent tuple (P_A, P_B), unless null rules (e.g. MATCH FULL / MATCH SIMPLE) apply.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In Prescription_Batches(Hospital_Code, Batch_No) referencing Master_Hospitals(Hospital_Code, Batch_No), what constitutes a valid child insert?",
        "options": [
          "A. Both Hospital_Code and Batch_No combined must match an existing row in Master_Hospitals",
          "B. Batch_No must be zero",
          "C. Hospital_Code alone matching is sufficient",
          "D. The tables must have identical row counts"
        ],
        "correct_option": "A",
        "explanation": "Composite foreign keys require full pairwise attribute matching in the referenced parent row."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In Account_Facility(Routing_No, Account_No) referencing Fed_Wire_Directory(Routing_No, Account_No):",
        "options": [
          "A. Both Routing_No and Account_No together must match a single registered wire directory entry",
          "B. Accounts cannot use routing numbers",
          "C. Composite keys are forbidden in finance",
          "D. Routing_No can be matched to any bank account in the world"
        ],
        "correct_option": "A",
        "explanation": "Pairwise matching ensures child accounts link to the precise parent banking institution."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In Marketplace_Inventory(Merchant_ID, SKU) referencing Merchant_Catalog(Merchant_ID, SKU):",
        "options": [
          "A. SKU alone matching any merchant is valid",
          "B. The exact (Merchant_ID, SKU) pair must exist in Merchant_Catalog",
          "C. Merchant_ID must be 1",
          "D. Price must be positive"
        ],
        "correct_option": "B",
        "explanation": "Composite references require dual-attribute matching to identify items within vendor catalogs."
      }
    ]
  },
  {
    "id": "MCQ-110",
    "title": "Multiple Foreign Keys & Referential Cycles",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Mutually Referencing Foreign Key Constraints",
    "difficulty": "Hard",
    "source": "UGC NET CSE Oct 2020 | Part 2 | Question: 99",
    "prompt": "When table Department has a foreign key Manager_ID referencing Employee(Emp_ID), and table Employee has a foreign key Dept_ID referencing Department(Dept_ID), how can initial records be inserted without violating referential integrity?",
    "options": [
      "A. It is mathematically impossible to insert records into mutually referencing tables",
      "B. By inserting one table with a NULL foreign key first (or using DEFERRABLE constraints that delay foreign key checking until COMMIT), then inserting the second table, and updating the first",
      "C. By dropping both tables",
      "D. By disabling database logging permanently"
    ],
    "correct_option": "B",
    "explanation": "Circular foreign key dependencies create an insertion deadlock under immediate constraint checking. Solutions include: (1) making at least one foreign key column nullable and inserting with NULL before back-populating, or (2) using 'DEFERRABLE INITIALLY DEFERRED' constraints checked only at transaction COMMIT.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Hospital Ward references Head_Doctor(Doc_ID), and Doctor references Assigned_Ward(Ward_ID). How does a DBA initialize a new ward and its head doctor?",
        "options": [
          "A. Insert Ward with Head_Doctor as NULL, insert Doctor referencing the Ward, then UPDATE Ward with the Doctor's ID within a transaction",
          "B. Bypass SQL validation using hex editing",
          "C. Delete all existing wards",
          "D. Create two identical databases"
        ],
        "correct_option": "A",
        "explanation": "Nulling one foreign key initially resolves circular insertion dependency deadlocks."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Trading_Desk references Lead_Trader(Trader_ID), and Trader references Assigned_Desk(Desk_ID). How are initial desk and trader records seeded?",
        "options": [
          "A. Using DEFERRABLE constraints within a single transaction, or inserting with NULL and updating afterwards",
          "B. By converting the database to MongoDB",
          "C. By creating traders without IDs",
          "D. By rebooting the banking cluster"
        ],
        "correct_option": "A",
        "explanation": "Deferred constraint checking delays foreign key validation until transaction commit."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Store_Branch references Manager_ID, and Staff references Branch_ID. How does onboarding seed the store?",
        "options": [
          "A. By ignoring foreign keys",
          "B. By inserting the branch with Manager_ID=NULL, adding the manager with Branch_ID, and updating the branch",
          "C. By running the query in reverse",
          "D. By deleting the store catalog"
        ],
        "correct_option": "B",
        "explanation": "Temporary nullification breaks circular referential dependency loops."
      }
    ]
  },
  {
    "id": "MCQ-111",
    "title": "SQL Schema Alteration with Foreign Key Constraints",
    "topic": "SQL Invariants & Declarative Constraints",
    "subtopic": "ALTER TABLE and Constraint Addition Rules",
    "difficulty": "Medium",
    "source": "UGC NET CSE Oct 2020 | Part 2 | Question: 100",
    "prompt": "If an administrator executes 'ALTER TABLE Child ADD CONSTRAINT fk_p FOREIGN KEY (P_ID) REFERENCES Parent(P_ID)' on a table already containing data, what check is performed by the database engine?",
    "options": [
      "A. The engine checks no data and applies the constraint only to future rows",
      "B. The engine validates all existing rows in Child; if any row has a P_ID that does not exist in Parent, the ALTER TABLE command fails and is rolled back",
      "C. The engine deletes all non-matching rows in Child automatically",
      "D. The engine populates missing rows in Parent with dummy data"
    ],
    "correct_option": "B",
    "explanation": "When adding an integrity constraint to an existing table, the database performs a full table validation scan. If existing data violates the constraint (orphan rows in Child), the ALTER TABLE statement is aborted, and no changes are saved.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When adding a foreign key from existing Prescriptions to Patients table, what happens if orphaned prescription records exist?",
        "options": [
          "A. The ALTER TABLE statement fails immediately, requiring the DBA to clean up orphan prescriptions first",
          "B. Orphan prescriptions are transferred to veterinary wards",
          "C. The database drops the Patients table",
          "D. The constraint is applied silently"
        ],
        "correct_option": "A",
        "explanation": "Validation scans fail if pre-existing data violates new foreign key rules."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Adding a foreign key constraint to an existing Transactions table referencing Accounts fails if:",
        "options": [
          "A. There are legacy transactions referencing deleted or non-existent account numbers",
          "B. The bank balance is positive",
          "C. Accounts table is empty",
          "D. The transactions table has indexes"
        ],
        "correct_option": "A",
        "explanation": "Relational engines reject new constraints when legacy data violates referential integrity."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Adding a foreign key between Reviews and Products tables will abort with an error if:",
        "options": [
          "A. Products have zero reviews",
          "B. Any existing review references a Product_ID that does not exist in Products",
          "C. Review ratings are between 1 and 5",
          "D. The web server is online"
        ],
        "correct_option": "B",
        "explanation": "Pre-existing orphan tuples prevent successful addition of foreign key constraints."
      }
    ]
  },
  {
    "id": "MCQ-112",
    "title": "Transaction Rollback & Log-Based Crash Recovery",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Crash Recovery and Transaction States",
    "difficulty": "Hard",
    "source": "UGC NET CSE Dec 2014 | Part 3 | Question: 09",
    "prompt": "During crash recovery using a Write-Ahead Log with checkpoints, which transactions must be UNDONE (rolled back)?",
    "options": [
      "A. All transactions that completed and committed before the checkpoint",
      "B. All transactions that were active (uncommitted) at the time of the crash",
      "C. All transactions recorded in the log from the start of the database",
      "D. Only read-only transactions"
    ],
    "correct_option": "B",
    "explanation": "During crash recovery, the Analysis phase populates the Active Transaction Table. Any transaction that began before or during the crash but did NOT write a COMMIT log record prior to system failure must be UNDONE to maintain the Atomicity property.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a hospital server crashes at 14:00, which clinical transactions must the recovery manager undo?",
        "options": [
          "A. Any patient chart updates that were in-progress and uncommitted at 14:00",
          "B. Discharged patient records",
          "C. All surgeries performed since morning",
          "D. Doctor payroll calculations"
        ],
        "correct_option": "A",
        "explanation": "Uncommitted active transactions at crash time must be completely rolled back."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Following a data center power outage, which wire transfers are undone during database restart?",
        "options": [
          "A. All wire transfer transactions that were actively executing and had not yet logged a COMMIT record",
          "B. Only international wire transfers",
          "C. None; all transactions are committed automatically",
          "D. All committed customer deposits"
        ],
        "correct_option": "A",
        "explanation": "Uncommitted financial transfers must be undone to prevent corrupted partial ledger states."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "After an e-commerce server crashes during a flash sale, which cart checkouts are undone?",
        "options": [
          "A. All orders placed during the entire day",
          "B. Checkouts that were active and uncommitted at the moment of the crash",
          "C. Only orders using credit cards",
          "D. Products that are out of stock"
        ],
        "correct_option": "B",
        "explanation": "The undo recovery pass cleans up uncommitted transactions active at crash time."
      }
    ]
  },
  {
    "id": "MCQ-113",
    "title": "ACID Atomicity Enforcement via Undo Logging",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Atomicity and Undo Log Mechanisms",
    "difficulty": "Medium",
    "source": "UGC NET CSE June 2012 | Part 2 | Question: 12",
    "prompt": "In database recovery managers, what information stored in an update log record is used by the recovery engine to execute an UNDO operation?",
    "options": [
      "A. The New Value (after-image) of the modified data item",
      "B. The Old Value (before-image) of the modified data item",
      "C. The IP address of the client terminal",
      "D. The user's operating system password"
    ],
    "correct_option": "B",
    "explanation": "Undo logging records the Before-Image (the Old Value) of modified data items. When rolling back an aborted or crashed transaction, the recovery manager writes the before-image back to the data item, reversing the uncommitted update.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "When rolling back an accidental prescription dosage increase from 10mg to 100mg, what does the recovery manager write back to the patient record?",
        "options": [
          "A. The before-image (10mg) recorded in the undo log",
          "B. The average hospital dose",
          "C. 0mg",
          "D. NULL"
        ],
        "correct_option": "A",
        "explanation": "Undo operations restore the before-image stored in the transaction log."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "To roll back an uncommitted debit of $500 from an account that originally had $2000, what log value does the engine apply?",
        "options": [
          "A. The before-image balance of $2000 from the undo log record",
          "B. $0",
          "C. $2500",
          "D. $1500"
        ],
        "correct_option": "A",
        "explanation": "Before-images restore pre-transaction financial balances upon rollback."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When undoing a stock reduction from 50 to 48 for an aborted checkout, what value is written to inventory?",
        "options": [
          "A. 48",
          "B. The before-image of 50 recorded in the WAL undo record",
          "C. 0",
          "D. 100"
        ],
        "correct_option": "B",
        "explanation": "Undo logging utilizes the before-image to restore pre-update stock counts."
      }
    ]
  },
  {
    "id": "MCQ-114",
    "title": "Concurrency Conflict Serializability Equivalence",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Conflict Equivalence and Non-conflicting Swaps",
    "difficulty": "Medium",
    "source": "UGC NET CSE Nov 2017 | Part 3 | Question: 7",
    "prompt": "Two transaction schedules S1 and S2 are defined as Conflict Equivalent if and only if:",
    "options": [
      "A. S1 and S2 contain the exact same transactions and order of all operations",
      "B. S1 can be transformed into S2 by a series of swaps of non-conflicting consecutive operations",
      "C. S1 and S2 produce the same final database state for only one specific initial state",
      "D. Both schedules use shared read locks exclusively"
    ],
    "correct_option": "B",
    "explanation": "Two schedules are conflict equivalent if the order of any two conflicting operations (read-write, write-read, write-write on the same data item by different transactions) is identical in both schedules, allowing one schedule to be transformed into the other by swapping adjacent non-conflicting operations.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical EMR charting, when are two concurrent doctor schedules conflict equivalent?",
        "options": [
          "A. When non-conflicting operations on different patient charts can be swapped to transform one schedule into the other without changing the relative order of conflicting chart updates",
          "B. When patient charts are deleted",
          "C. When doctors write identical medical notes",
          "D. When doctors log in at the same minute"
        ],
        "correct_option": "A",
        "explanation": "Conflict equivalence preserves the ordering of all conflicting operations."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In banking ledger schedules, two transaction orderings are conflict equivalent if:",
        "options": [
          "A. They maintain identical relative ordering for all conflicting operations on common accounts",
          "B. Wire transfers are encrypted with AES-256",
          "C. All accounts belong to the same bank",
          "D. Both ledgers have zero balances"
        ],
        "correct_option": "A",
        "explanation": "Swapping non-conflicting independent account updates yields conflict equivalent schedules."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Two order processing schedules are conflict equivalent if:",
        "options": [
          "A. All orders are free",
          "B. Swapping operations on distinct inventory items transforms one schedule into the other while preserving conflicting access orders on shared items",
          "C. Every cart contains one item",
          "D. Checkout takes less than 1 second"
        ],
        "correct_option": "B",
        "explanation": "Conflict equivalence guarantees schedules preserve relative order on shared conflicting data items."
      }
    ]
  },
  {
    "id": "MCQ-115",
    "title": "View Serializability & Blind Writes",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "View Serializability and Blind Write Invariants",
    "difficulty": "Hard",
    "source": "UGC NET CSE June 2023 | Part 2: 44",
    "prompt": "What condition allows a concurrent schedule to be View Serializable but NOT Conflict Serializable?",
    "options": [
      "A. The presence of shared read locks",
      "B. The presence of 'Blind Writes' (writing a data item without reading it first)",
      "C. Having only one transaction",
      "D. Using B-tree indexes"
    ],
    "correct_option": "B",
    "explanation": "If a schedule has no blind writes, conflict serializability and view serializability are completely identical. A schedule can be view serializable without being conflict serializable ONLY if it contains blind writes (write(X) without prior read(X)), which can satisfy view equivalence despite cycles in conflict graphs.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In sensor telemetry logging, an automated sensor overwrites oxygen saturation without reading previous values (blind write). This allows the schedule to:",
        "options": [
          "A. Achieve view serializability even if conflict serializability graph contains cycles",
          "B. Cause physical pacemaker failure",
          "C. Corrupt the entire medical database",
          "D. Bypass SQL syntax validation"
        ],
        "correct_option": "A",
        "explanation": "Blind writes decouple view serializability from strict conflict serializability."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In automated foreign exchange feeds, tick data blind-writes currency rates. How does this impact serializability?",
        "options": [
          "A. The schedule can be view serializable despite conflict graph cycles",
          "B. The exchange must shut down",
          "C. Transactions must use 3-phase commit",
          "D. It causes immediate database corruption"
        ],
        "correct_option": "A",
        "explanation": "Blind writes permit view serializability where conflict serializability tests fail."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "A batch job resets product promotion counters without reading past values. This blind write allows:",
        "options": [
          "A. Unlimited discount generation",
          "B. View serializability without satisfying conflict serializability",
          "C. Disabling database transactions",
          "D. Bypassing disk writes"
        ],
        "correct_option": "B",
        "explanation": "Blind writes create view-equivalent schedules that violate conflict graph acyclicity."
      }
    ]
  },
  {
    "id": "MCQ-116",
    "title": "Strict Two-Phase Locking vs Rigorous 2PL",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Rigorous 2PL and Lock Holding Policies",
    "difficulty": "Hard",
    "source": "UGC NET CSE Oct 2020 | Part 2 | Question: 48",
    "prompt": "How does 'Rigorous Two-Phase Locking' (Rigorous 2PL) differ from 'Strict 2PL' in relational transaction managers?",
    "options": [
      "A. Strict 2PL holds exclusive locks until commit, whereas Rigorous 2PL holds BOTH shared read locks AND exclusive write locks until transaction termination",
      "B. Rigorous 2PL allows locks to be released before commit",
      "C. Strict 2PL requires no lock manager",
      "D. Rigorous 2PL causes deadlocks in all schedules"
    ],
    "correct_option": "A",
    "explanation": "In Strict 2PL, all exclusive (X) write locks are held until commit/abort, but shared (S) read locks can be released earlier during the shrinking phase. In Rigorous 2PL, ALL locks (both shared and exclusive) must be held until the transaction commits or aborts, ensuring serializability order matches commit order.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why do high-security hospital research databases enforce Rigorous 2PL for clinical trials?",
        "options": [
          "A. Because doctors cannot read locked charts",
          "B. Holding both read and write locks until commit ensures transaction serialization order matches the exact physical commit timestamp order",
          "C. To prevent data from being saved",
          "D. Because medical databases only support exclusive locks"
        ],
        "correct_option": "B",
        "explanation": "Rigorous 2PL holds all shared and exclusive locks until commit, guaranteeing strict serializability."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In high-audit banking platforms, what extra guarantee does Rigorous 2PL provide over Strict 2PL?",
        "options": [
          "A. It eliminates credit limits",
          "B. It speeds up ATM cash ejection",
          "C. It holds read locks until commit, guaranteeing transactions serialize in the exact order they commit",
          "D. It removes the need for transaction rollbacks"
        ],
        "correct_option": "C",
        "explanation": "Rigorous 2PL aligns serialization order with commit order by holding all read and write locks."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In inventory reservation systems, why is Rigorous 2PL used during flash sales?",
        "options": [
          "A. To allow customers to hold items forever",
          "B. Because flash sales forbid database locks",
          "C. To double server memory",
          "D. Holding both read and write locks until transaction termination prevents non-repeatable reads and aligns order commitment sequences"
        ],
        "correct_option": "D",
        "explanation": "Rigorous 2PL prevents any lock release prior to commit, guaranteeing strict serialization order."
      }
    ]
  },
  {
    "id": "MCQ-117",
    "title": "Active Database Architecture: Event Detection",
    "topic": "Triggers & Active Databases",
    "subtopic": "Active Database Subsystems and Event Detectors",
    "difficulty": "Medium",
    "source": "UGC NET CSE Dec 2013 | Part 2 | Question: 12",
    "prompt": "In an Active Database Management System, which specialized subsystem is responsible for monitoring operations and signaling that a trigger's Event has taken place?",
    "options": [
      "A. Event Detector",
      "B. Query Optimizer",
      "C. Lock Manager",
      "D. Buffer Pool Manager"
    ],
    "correct_option": "A",
    "explanation": "An Active DBMS augments conventional passive DBMS engines with an Event Detector subsystem. The Event Detector monitors primitive events (database DML like INSERT/UPDATE/DELETE, clock events, or external signals) and signals the Rule Execution Engine when an ECA event is triggered.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a clinical active database, what component detects when an ICU nurse updates patient intracranial pressure above safe thresholds?",
        "options": [
          "A. The hospital air conditioning unit",
          "B. The Event Detector subsystem monitoring database DML operations",
          "C. The SQL grammar tokenizer",
          "D. The display screen backlight"
        ],
        "correct_option": "B",
        "explanation": "Event Detectors signal active database engines when critical clinical thresholds are crossed."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In a real-time fraud monitoring database, what component catches rapid consecutive ATM withdrawals across different states?",
        "options": [
          "A. The disk head motor",
          "B. The database backup tape",
          "C. The Event Detector module of the active database engine",
          "D. The printer spooler"
        ],
        "correct_option": "C",
        "explanation": "Event Detectors monitor transaction streams to signal rule evaluation engines."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In an inventory active database, what component signals when warehouse stock drops below safety margins?",
        "options": [
          "A. The customer web browser",
          "B. The optical fiber transceiver",
          "C. The SQL parser's syntax checker",
          "D. The Event Detector subsystem of the active DBMS"
        ],
        "correct_option": "D",
        "explanation": "Event Detectors identify triggering threshold events and notify rule execution managers."
      }
    ]
  },
  {
    "id": "MCQ-118",
    "title": "Row-Level Triggers vs Statement-Level Triggers",
    "topic": "Triggers & Active Databases",
    "subtopic": "FOR EACH ROW vs FOR EACH STATEMENT Invariants",
    "difficulty": "Medium",
    "source": "UGC NET CSE Dec 2013 | Part 3 | Question: 60",
    "prompt": "If an SQL statement 'UPDATE Employees SET Salary = Salary * 1.1 WHERE Dept_ID = 10' updates 50 employee records, how many times will a 'FOR EACH ROW' trigger execute compared to a 'FOR EACH STATEMENT' trigger?",
    "options": [
      "A. FOR EACH ROW executes 50 times; FOR EACH STATEMENT executes 1 time",
      "B. Both triggers execute 50 times",
      "C. Both triggers execute 1 time",
      "D. FOR EACH ROW executes 1 time; FOR EACH STATEMENT executes 50 times"
    ],
    "correct_option": "A",
    "explanation": "A row-level trigger (declared with 'FOR EACH ROW') fires once for every individual row modified by the SQL statement (50 times). A statement-level trigger (the default 'FOR EACH STATEMENT') fires exactly once per executing SQL statement regardless of how many rows are modified (1 time).",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A batch update updates the medication dosages of 40 ICU patients simultaneously. How many times will an 'AFTER UPDATE FOR EACH ROW' audit trigger fire?",
        "options": [
          "A. Exactly 1 time",
          "B. Exactly 40 times (once for each modified patient row)",
          "C. 0 times",
          "D. 1600 times"
        ],
        "correct_option": "B",
        "explanation": "Row-level triggers fire once per affected tuple, logging all 40 patient modifications."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "An end-of-month interest posting updates 10,000 savings accounts in a single SQL statement. How many times does a statement-level trigger fire?",
        "options": [
          "A. 10,000 times",
          "B. 0 times",
          "C. Exactly 1 time for the entire SQL statement",
          "D. Once per bank branch"
        ],
        "correct_option": "C",
        "explanation": "Statement-level triggers fire once per SQL operation, ideal for batch logging."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "A flash sale discount updates the price of 200 catalog products in one command. An 'AFTER UPDATE FOR EACH ROW' trigger fires:",
        "options": [
          "A. 1 time",
          "B. Only for products priced over $100",
          "C. 0 times",
          "D. 200 times, auditing each product's price change individually"
        ],
        "correct_option": "D",
        "explanation": "Row-level triggers execute per modified record, providing granular per-product audit trails."
      }
    ]
  },
  {
    "id": "MCQ-119",
    "title": "BEFORE INSERT Triggers: Data Sanitization & Invariants",
    "topic": "Triggers & Active Databases",
    "subtopic": "BEFORE Trigger Capabilities and Modifying NEW",
    "difficulty": "Medium",
    "source": "UGC NET CSE June 2009 | Paper 2: 23",
    "prompt": "What unique capability does a 'BEFORE INSERT' row-level trigger possess in relational database engines (such as PostgreSQL and Oracle) that an 'AFTER INSERT' trigger does NOT possess?",
    "options": [
      "A. It can modify the attributes of the 'NEW' record pseudo-variable before the tuple is written to the table",
      "B. It can drop the table",
      "C. It runs without acquiring database locks",
      "D. It can view deleted historical rows"
    ],
    "correct_option": "A",
    "explanation": "A BEFORE INSERT row-level trigger can inspect and directly modify fields of the 'NEW' pseudo-record (e.g. sanitizing input, populating defaults, converting text to uppercase). AFTER triggers fire after the row is committed to storage, where NEW is read-only.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Why does a clinical EMR use a BEFORE INSERT trigger on Patient_Intake rather than an AFTER INSERT trigger?",
        "options": [
          "A. Because AFTER triggers cannot read patient data",
          "B. To automatically standardize and format patient telephone numbers and capitalize names on the NEW record before storage",
          "C. To delete the patient record immediately",
          "D. To print patient ID cards"
        ],
        "correct_option": "B",
        "explanation": "BEFORE triggers sanitize and format NEW patient record values prior to physical insertion."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why is a BEFORE INSERT trigger used on Wire_Transactions to strip illegal whitespace and validate routing codes?",
        "options": [
          "A. Because banks cannot use AFTER triggers",
          "B. To prevent the wire from executing",
          "C. Because BEFORE triggers can modify the NEW transaction tuple before it is persisted to disk",
          "D. To double the transaction fee"
        ],
        "correct_option": "C",
        "explanation": "Modifying NEW values during BEFORE triggers guarantees clean data ingestion."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "How does an e-commerce platform automatically compute and populate Tax_Amount on incoming order rows?",
        "options": [
          "A. Using an AFTER DELETE trigger",
          "B. By asking the customer to calculate tax manually",
          "C. Using a foreign key constraint",
          "D. Using a BEFORE INSERT trigger that calculates tax and assigns it directly to NEW.Tax_Amount before writing the row"
        ],
        "correct_option": "D",
        "explanation": "BEFORE triggers populate derived columns directly into the NEW row prior to storage."
      }
    ]
  },
  {
    "id": "MCQ-120",
    "title": "AFTER UPDATE Triggers: Automated Audit Trail Logging",
    "topic": "Triggers & Active Databases",
    "subtopic": "Audit Trail Generation using AFTER Triggers",
    "difficulty": "Medium",
    "source": "UGC NET CSE July 2018 | Part 2 | Question: 68",
    "prompt": "Why are 'AFTER UPDATE' triggers preferred over 'BEFORE UPDATE' triggers for recording historical change audit logs?",
    "options": [
      "A. AFTER triggers only run when the table is empty",
      "B. AFTER triggers fire only after the update has passed all declarative constraints and is guaranteed to succeed, preventing phantom audit entries for aborted updates",
      "C. BEFORE triggers cannot read the OLD record pseudo-variable",
      "D. AFTER triggers run with superuser permissions automatically"
    ],
    "correct_option": "B",
    "explanation": "An AFTER UPDATE trigger fires after the data modification has passed all constraint checks (foreign keys, check constraints) and has successfully updated the row. This ensures the audit table only logs genuine, non-aborted changes.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical charting, why does an EMR use an AFTER UPDATE trigger on Patient_Prescriptions to record dosage modifications in Prescription_Audit?",
        "options": [
          "A. To ensure audit entries are logged only for modifications that successfully satisfy clinical validation constraints",
          "B. Because BEFORE triggers cannot write to other tables",
          "C. To delete the prescription if the doctor makes a mistake",
          "D. To slow down prescription processing"
        ],
        "correct_option": "A",
        "explanation": "AFTER triggers log audit records only after dosage updates successfully pass all constraint checks."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why does a core banking ledger log balance changes to Ledger_Audit using an AFTER UPDATE trigger rather than a BEFORE trigger?",
        "options": [
          "A. To prevent logging false audit entries if the balance update subsequently aborts due to a negative balance constraint",
          "B. To allow tellers to modify past audit logs",
          "C. To convert transactions into crypto tokens",
          "D. Because BEFORE triggers are forbidden in financial databases"
        ],
        "correct_option": "A",
        "explanation": "AFTER triggers prevent ghost audit records for transactions that fail subsequent validation."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "When catalog item prices are changed, why is Price_History populated via an AFTER UPDATE trigger?",
        "options": [
          "A. It refunds customers who bought the item earlier",
          "B. It guarantees price history rows are recorded only when the price update successfully commits",
          "C. It speeds up search indexing",
          "D. It removes the item from the shopping cart"
        ],
        "correct_option": "B",
        "explanation": "AFTER triggers ensure audit histories reflect successfully verified price modifications."
      }
    ]
  },
  {
    "id": "MCQ-121",
    "title": "INSTEAD OF Triggers on Non-Updatable Complex Views",
    "topic": "Triggers & Active Databases",
    "subtopic": "INSTEAD OF Triggers on Multi-Table Views",
    "difficulty": "Hard",
    "source": "UGC NET CSE July 2016 | Part 2 | Question: 20",
    "prompt": "What is the primary architectural purpose of an 'INSTEAD OF' trigger in relational database management systems?",
    "options": [
      "A. Replacing deleted data with dummy data",
      "B. Intercepting DML operations (INSERT, UPDATE, DELETE) on non-updatable complex views and executing custom procedural code to modify underlying base tables",
      "C. Replacing B-tree indexes with hash tables",
      "D. Replacing SQL with Python syntax"
    ],
    "correct_option": "B",
    "explanation": "Complex views containing joins, aggregations, or unions cannot be updated directly by standard SQL DML. An INSTEAD OF trigger intercepts the DML operation on the view and executes custom procedural SQL that routes and applies the modifications to the appropriate underlying base tables.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital creates a complex view 'Patient_Summary' joining Patients, Insurance, and Attending_Physician. How can an administrator make this view writable?",
        "options": [
          "A. By defining INSTEAD OF INSERT/UPDATE triggers on Patient_Summary that split and route updates to the separate base tables",
          "B. By dropping the primary keys of the base tables",
          "C. By converting all patient data to text files",
          "D. By creating a database link"
        ],
        "correct_option": "A",
        "explanation": "INSTEAD OF triggers enable transparent writes on multi-table medical views."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In banking, a consolidated view 'Client_Financial_Profile' joins Checking, Savings, and Loans. How can client address updates be processed through this view?",
        "options": [
          "A. Using an INSTEAD OF UPDATE trigger that directs address updates to the master Customer_Profiles table",
          "B. By disabling database security",
          "C. By recalculating customer credit scores",
          "D. By merging all accounts into checking"
        ],
        "correct_option": "A",
        "explanation": "INSTEAD OF triggers route updates on complex financial views to underlying entity tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "An e-commerce reporting view joins Products, Inventory, and Supplier_Catalog. How can merchant stock updates through this view be enabled?",
        "options": [
          "A. By deleting the Supplier_Catalog table",
          "B. An INSTEAD OF UPDATE trigger intercepts the view update and modifies the physical Inventory base table",
          "C. By turning off referential integrity",
          "D. By clearing all customer shopping carts"
        ],
        "correct_option": "B",
        "explanation": "INSTEAD OF triggers bridge the gap between complex analytical views and normalized base tables."
      }
    ]
  },
  {
    "id": "MCQ-122",
    "title": "Recursive Triggers & Cascading Trigger Depths",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Cascading and Infinite Recursion",
    "difficulty": "Hard",
    "source": "UGC NET CSE June 2019 | Part 2 | Question: 35",
    "prompt": "What occurs when Trigger A updates Table 2, firing Trigger B which updates Table 1, firing Trigger A again?",
    "options": [
      "A. The database executes the cycle indefinitely until physical RAM burns out",
      "B. The DBMS detects an infinite recursive trigger cascade, aborts the operation when the maximum trigger recursion depth is reached, and rolls back the transaction",
      "C. The database engine converts the trigger to a stored procedure",
      "D. The updates are saved in reverse chronological order"
    ],
    "correct_option": "B",
    "explanation": "Database management systems maintain a maximum trigger nesting/recursion depth counter (e.g. 16 or 32 levels). If cascading triggers form an infinite loop, the engine raises a recursion depth exceeded exception, aborting and rolling back the initiating transaction.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If an update to Patient_Ward fires a trigger that updates Bed_Status, which triggers an update back to Patient_Ward: how does PostgreSQL respond?",
        "options": [
          "A. It raises a trigger recursion limit exceeded error and rolls back the entire transaction",
          "B. It discharges all ward patients",
          "C. It creates 10,000 duplicate beds",
          "D. It shuts down the hospital electrical grid"
        ],
        "correct_option": "A",
        "explanation": "DBMS engines catch circular trigger cascades, aborting before memory exhaustion."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In wire settlement, if Trigger T_Debit updates Account B firing T_Credit which updates Account A: what prevents an infinite balance loop?",
        "options": [
          "A. The engine enforces maximum trigger nesting depth limits, throwing an error and rolling back the wire",
          "B. The database converts to an unindexed tape",
          "C. Tellers are locked out",
          "D. Account balances automatically reset to $0"
        ],
        "correct_option": "A",
        "explanation": "Recursion depth tracking prevents infinite trigger loops in financial transactions."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If updating Cart triggers an Inventory update, which triggers a Cart coupon update in a loop, how is disaster avoided?",
        "options": [
          "A. All products become free",
          "B. The database aborts the transaction when trigger recursion depth limit is exceeded",
          "C. Customer is charged infinitely",
          "D. The products table is truncated"
        ],
        "correct_option": "B",
        "explanation": "Nesting limits terminate cascading trigger loops and protect relational state."
      }
    ]
  },
  {
    "id": "MCQ-123",
    "title": "Database Roles: CREATE ROLE & GRANT ROLE Hierarchy",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Inheritance",
    "difficulty": "Medium",
    "source": "UGC NET CSE Dec 2008 | Part 2 | Question: 34",
    "prompt": "In enterprise Role-Based Access Control (RBAC), how is role inheritance established in SQL standard syntax?",
    "options": [
      "A. CREATE ROLE <child> EXTENDS <parent>;",
      "B. GRANT <parent_role> TO <child_role>;",
      "C. ALTER ROLE <child> INHERIT <parent>;",
      "D. SET ROLE <parent> INTO <child>;"
    ],
    "correct_option": "B",
    "explanation": "In standard SQL RBAC implementations: 'GRANT parent_role TO child_role;' establishes role hierarchy. Any user granted child_role automatically inherits all permissions and privileges possessed by parent_role, enabling structured, hierarchical access control.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In a hospital RBAC schema, how does the DBA configure the 'Chief_Surgeon' role to inherit all permissions of the base 'Physician' role?",
        "options": [
          "A. GRANT Physician TO Chief_Surgeon;",
          "B. CREATE SURGEON AS PHYSICIAN;",
          "C. MERGE Physician INTO Chief_Surgeon;",
          "D. DROP ROLE Physician;"
        ],
        "correct_option": "A",
        "explanation": "GRANT Physician TO Chief_Surgeon establishes hierarchical clinical privilege inheritance."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "To allow the 'Senior_Branch_Manager' role to inherit all capabilities of the 'Teller' role in a bank database:",
        "options": [
          "A. GRANT Teller TO Senior_Branch_Manager;",
          "B. ALTER USER Teller RENAME Senior_Branch_Manager;",
          "C. CREATE VIEW Manager_Teller AS SELECT 1;",
          "D. SET ROLE Senior_Branch_Manager = Teller;"
        ],
        "correct_option": "A",
        "explanation": "Role granting constructs clean inheritance hierarchies in financial access governance."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "To ensure 'Store_Admin' automatically inherits all catalog editing rights of 'Catalog_Editor':",
        "options": [
          "A. LINK Catalog_Editor WITH Store_Admin;",
          "B. GRANT Catalog_Editor TO Store_Admin;",
          "C. ALTER TABLE Products SET ADMIN = EDITOR;",
          "D. REVOKE Catalog_Editor FROM PUBLIC;"
        ],
        "correct_option": "B",
        "explanation": "Granting roles to other roles builds modular, reusable permission hierarchies."
      }
    ]
  },
  {
    "id": "MCQ-124",
    "title": "Privilege Revocation: RESTRICT vs CASCADE Invariants",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "REVOKE RESTRICT Safety Semantics",
    "difficulty": "Medium",
    "source": "UGC NET CSE Dec 2009 | Part 2 | Question: 20",
    "prompt": "Under the SQL standard, what occurs if an administrator executes 'REVOKE SELECT ON Table1 FROM UserA RESTRICT' when User A has previously granted SELECT to User B?",
    "options": [
      "A. SELECT is revoked from User A and User B simultaneously",
      "B. The REVOKE statement fails immediately with an error and no privileges are revoked",
      "C. User B becomes the owner of Table1",
      "D. Table1 is locked in read-only mode"
    ],
    "correct_option": "B",
    "explanation": "REVOKE ... RESTRICT is a defensive safety option. If revoking the privilege would cause dependent permissions held by other users (User B) to be abandoned or invalidated, the RESTRICT keyword causes the entire REVOKE statement to fail and abort with an error.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "A hospital DBA attempts: 'REVOKE SELECT ON Patient_Charts FROM Head_Nurse RESTRICT'. If Head_Nurse has delegated chart viewing to 10 shift nurses, what happens?",
        "options": [
          "A. The command fails and aborts, preventing accidental cascading loss of chart access for the shift nurses",
          "B. Patient charts are made public",
          "C. All 10 shift nurses are fired",
          "D. Head Nurse is demoted to patient"
        ],
        "correct_option": "A",
        "explanation": "RESTRICT prevents accidental revocation when dependent delegated grants exist."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a compliance officer executes 'REVOKE INSERT ON Wire_Transfers FROM Lead_Broker RESTRICT' while junior brokers hold delegated rights:",
        "options": [
          "A. The command aborts with an error, requiring explicit CASCADE if dependent grants are to be removed",
          "B. Bank ledger is rolled back 24 hours",
          "C. Wire transfers are deleted",
          "D. Junior brokers can wire money with no limit"
        ],
        "correct_option": "A",
        "explanation": "REVOKE RESTRICT guarantees that privilege revocations do not break downstream operational workflows."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Executing 'REVOKE UPDATE ON Products FROM Inventory_Lead RESTRICT' when the lead has granted update rights to packing staff results in:",
        "options": [
          "A. Automatic promotion of packing staff",
          "B. An immediate error abortion, preserving packing staff access until explicitly handled",
          "C. Products table being converted to CSV",
          "D. Deletion of all product prices"
        ],
        "correct_option": "B",
        "explanation": "RESTRICT blocks revocations that have downstream authorization dependencies."
      }
    ]
  },
  {
    "id": "MCQ-125",
    "title": "WITH GRANT OPTION Delegation Chains & Cycles",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Delegation Chains and Dual Path Grants",
    "difficulty": "Hard",
    "source": "UGC NET CSE Jan 2017 | Part 2 | Question: 47",
    "prompt": "User A grants privilege P with grant option to User B. User B grants P to User C. Independently, User D (who also holds P with grant option) grants P to User C. If User A revokes P from User B CASCADE, what happens to User C's privilege?",
    "options": [
      "A. User C loses privilege P completely",
      "B. User C retains privilege P because an independent authorization path from User D still exists",
      "C. User C loses half of their permissions",
      "D. Both User B and User D are revoked"
    ],
    "correct_option": "B",
    "explanation": "In relational authorization graphs, a user retains a privilege as long as there exists at least one valid path from an independent granter in the authorization dependency DAG. Since User D independently granted P to C, revoking B's path does not revoke C's privilege.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "Nurse C receives patient chart viewing rights from Dr. A (via Nurse B) AND independently from Chief Surgeon D. If Dr. A revokes B CASCADE, what happens to Nurse C?",
        "options": [
          "A. Nurse C retains chart viewing rights through Chief Surgeon D's independent authorization path",
          "B. Nurse C's badge is deactivated",
          "C. Nurse C is logged out forever",
          "D. Hospital data is wiped"
        ],
        "correct_option": "A",
        "explanation": "Multi-path authorization graphs ensure users retain rights supported by independent grant paths."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Trader C receives wire rights from Manager B (granted by A) and independently from Compliance Officer D. If A revokes B CASCADE:",
        "options": [
          "A. Trader C continues to hold wire rights via Officer D's independent grant",
          "B. Wire transfers are frozen nationwide",
          "C. Officer D's rights are revoked",
          "D. Trader C's computer locks up"
        ],
        "correct_option": "A",
        "explanation": "Independent authorization paths preserve access rights when one granter path is dismantled."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Vendor C receives catalog rights from Team Lead B (granted by Admin A) and independently from Partner Manager D. When A revokes B CASCADE:",
        "options": [
          "A. Vendor C loses catalog access",
          "B. Vendor C retains catalog rights through Partner Manager D's grant",
          "C. Product prices are doubled",
          "D. The marketplace goes offline"
        ],
        "correct_option": "B",
        "explanation": "Authorization DAG traversal preserves privileges backed by surviving grant paths."
      }
    ]
  },
  {
    "id": "MCQ-126",
    "title": "Mandatory Access Control: Bell-LaPadula Simple Security",
    "topic": "Operating Systems: Security & Access Control",
    "subtopic": "Multi-Level Security Models and Classifications",
    "difficulty": "Medium",
    "source": "UGC NET CSE June 2012 | Part 3 | Question: 8",
    "prompt": "In multi-level security systems conforming to the Bell-LaPadula model, why is a subject with 'Secret' clearance forbidden from writing data into an 'Unclassified' document (No Write-Down)?",
    "options": [
      "A. To prevent the user from wasting hard disk space",
      "B. To prevent the illicit declassification or leakage of confidential information into lower-security publicly accessible channels",
      "C. Because unclassified documents cannot store binary characters",
      "D. Because Secret users can only read, not write"
    ],
    "correct_option": "B",
    "explanation": "The *-Property ('No Write-Down') in Bell-LaPadula protects confidentiality. It prevents a Trojan horse or malicious insider holding Secret clearance from copying classified data into an Unclassified document where uncleared subjects could read it.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In an epidemic research database, why cannot a researcher with 'Restricted Patient DNA' clearance write data into a 'Public Health Bulletin' table?",
        "options": [
          "A. The No Write-Down rule prevents accidental or malicious leakage of classified patient genomic data into public channels",
          "B. To prevent researchers from publishing papers",
          "C. Because genomic data is stored in letters A, C, T, G",
          "D. Because public tables are read-only"
        ],
        "correct_option": "A",
        "explanation": "No Write-Down prevents confidential medical data from leaking into public domains."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why cannot an M&A investment banker with 'Confidential Merger' clearance write into the 'Public Stock Recommendation' blog?",
        "options": [
          "A. To enforce the No Write-Down invariant, preventing insider merger details from leaking to the open market",
          "B. To save internet bandwidth",
          "C. Because public blogs use HTTP instead of HTTPS",
          "D. Because bankers cannot type on blogs"
        ],
        "correct_option": "A",
        "explanation": "Bell-LaPadula *-Property stops high-clearance subjects from leaking secrets into lower sinks."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why is a fraud intelligence analyst forbidden from writing confidential blacklisted payment signatures into a public merchant FAQ?",
        "options": [
          "A. Because merchants cannot read FAQs",
          "B. The No Write-Down security property protects sensitive fraud detection rules from being exposed to cybercriminals",
          "C. To allow cybercriminals to test credit cards",
          "D. Because databases forbid text files"
        ],
        "correct_option": "B",
        "explanation": "Multi-level security forbids downward writes to safeguard operational intelligence."
      }
    ]
  },
  {
    "id": "MCQ-127",
    "title": "Relational Integrity & Cascade Semantics #1",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 51",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 101)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 101)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 101)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 101)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-128",
    "title": "Relational Integrity & Cascade Semantics #2",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 52",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 102)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 102)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 102)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 102)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-129",
    "title": "Relational Integrity & Cascade Semantics #3",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 53",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 103)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 103)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 103)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 103)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-130",
    "title": "Relational Integrity & Cascade Semantics #4",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 54",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 104)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 104)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 104)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 104)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-131",
    "title": "Relational Integrity & Cascade Semantics #5",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 55",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 105)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 105)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 105)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 105)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-132",
    "title": "Relational Integrity & Cascade Semantics #6",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 56",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 106)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 106)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 106)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 106)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-133",
    "title": "Relational Integrity & Cascade Semantics #7",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 57",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 107)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 107)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 107)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 107)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-134",
    "title": "Relational Integrity & Cascade Semantics #8",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 58",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 108)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 108)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 108)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 108)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-135",
    "title": "Relational Integrity & Cascade Semantics #9",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 59",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 109)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 109)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 109)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 109)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-136",
    "title": "Relational Integrity & Cascade Semantics #10",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 60",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 110)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 110)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 110)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 110)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-137",
    "title": "Relational Integrity & Cascade Semantics #11",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 61",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 111)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 111)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 111)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 111)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-138",
    "title": "Relational Integrity & Cascade Semantics #12",
    "topic": "Referential Integrity & Cascades",
    "subtopic": "Referential Actions & Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 62",
    "prompt": "In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 112)?",
    "options": [
      "A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist",
      "B. RESTRICT deletes child records automatically",
      "C. CASCADE converts foreign keys to NULL",
      "D. Both actions disable foreign key checking"
    ],
    "correct_option": "A",
    "explanation": "ON UPDATE CASCADE automatically synchronizes child foreign key values with updated parent keys; RESTRICT rejects the update if any child rows reference the old key.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical records, when updating a hospital Department_ID from D10 to D20, how does ON UPDATE CASCADE preserve Doctor_Assignments (Case 112)?",
        "options": [
          "A. It deletes all assigned doctors",
          "B. It updates Doctor_Assignments.Dept_ID to D20 automatically, preserving doctor-ward associations",
          "C. It sets doctor names to NULL",
          "D. It shuts down the hospital database"
        ],
        "correct_option": "B",
        "explanation": "ON UPDATE CASCADE propagates Department_ID updates to all assigned doctor rows."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "When updating Account_Number on a master account, how does ON UPDATE CASCADE protect audit records (Case 112)?",
        "options": [
          "A. It resets balances to zero",
          "B. It freezes the customer account",
          "C. It propagates the new account number to all referencing child transaction rows simultaneously",
          "D. It converts checking accounts to savings"
        ],
        "correct_option": "C",
        "explanation": "Cascading updates maintain consistent foreign key links across financial audit tables."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In e-commerce inventory, when renaming a Manufacturer_ID, how does ON UPDATE CASCADE update Products (Case 112)?",
        "options": [
          "A. It cancels all customer orders",
          "B. It marks products as discontinued",
          "C. It doubles product prices",
          "D. It automatically updates Manufacturer_ID in all linked catalog product rows"
        ],
        "correct_option": "D",
        "explanation": "Cascading updates synchronize manufacturer keys across all referencing catalog records."
      }
    ]
  },
  {
    "id": "MCQ-139",
    "title": "Database Trigger Lifecycle & Timing Invariants #1",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 43",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 113)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 113)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 113)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 113)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-140",
    "title": "Database Trigger Lifecycle & Timing Invariants #2",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 44",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 114)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 114)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 114)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 114)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-141",
    "title": "Database Trigger Lifecycle & Timing Invariants #3",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 45",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 115)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 115)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 115)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 115)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-142",
    "title": "Database Trigger Lifecycle & Timing Invariants #4",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 46",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 116)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 116)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 116)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 116)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-143",
    "title": "Database Trigger Lifecycle & Timing Invariants #5",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 47",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 117)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 117)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 117)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 117)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-144",
    "title": "Database Trigger Lifecycle & Timing Invariants #6",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 48",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 118)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 118)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 118)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 118)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-145",
    "title": "Database Trigger Lifecycle & Timing Invariants #7",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 49",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 119)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 119)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 119)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 119)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-146",
    "title": "Database Trigger Lifecycle & Timing Invariants #8",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 50",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 120)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 120)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 120)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 120)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-147",
    "title": "Database Trigger Lifecycle & Timing Invariants #9",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 51",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 121)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 121)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 121)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 121)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-148",
    "title": "Database Trigger Lifecycle & Timing Invariants #10",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 52",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 122)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 122)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 122)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 122)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-149",
    "title": "Database Trigger Lifecycle & Timing Invariants #11",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 53",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 123)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 123)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 123)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 123)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-150",
    "title": "Database Trigger Lifecycle & Timing Invariants #12",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 54",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 124)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 124)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 124)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 124)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-151",
    "title": "Database Trigger Lifecycle & Timing Invariants #13",
    "topic": "Triggers & Active Databases",
    "subtopic": "Trigger Event Timing & Side Effect Isolation",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 55",
    "prompt": "In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 125)?",
    "options": [
      "A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement",
      "B. BEFORE trigger side effects are permanently saved even if the statement fails",
      "C. AFTER triggers execute before constraints are evaluated",
      "D. Triggers run in a completely unlogged memory buffer"
    ],
    "correct_option": "A",
    "explanation": "Under relational transactional ACID semantics, triggers execute within the boundary of the triggering statement's transaction. If a constraint or error aborts the statement, all changes made by triggers are atomically rolled back.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "If a BEFORE INSERT trigger logs an entry to Patient_Log but the patient insert violates a UNIQUE SSN constraint, what happens (Case 125)?",
        "options": [
          "A. The Patient_Log entry remains permanently on disk",
          "B. The entire transaction rolls back, erasing the Patient_Log entry to maintain atomicity",
          "C. The duplicate SSN is accepted anyway",
          "D. The patient table is locked forever"
        ],
        "correct_option": "B",
        "explanation": "Transaction rollback reverses all trigger modifications when constraint checks fail."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "If a trigger updates a teller audit count but the cash transfer violates a minimum balance rule, what happens (Case 125)?",
        "options": [
          "A. The teller is credited the transfer amount",
          "B. The database drops the audit table",
          "C. The audit update is rolled back with the transfer, leaving no phantom audit record",
          "D. The bank account balance becomes negative"
        ],
        "correct_option": "C",
        "explanation": "Transactional atomicity rolls back trigger side effects if the core transaction aborts."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "If an order trigger reserves inventory but the cart checkout fails credit authorization, what occurs (Case 125)?",
        "options": [
          "A. Stock remains reserved permanently",
          "B. The customer is charged a penalty",
          "C. The item is mailed for free",
          "D. The inventory reservation is automatically rolled back, returning stock to the catalog"
        ],
        "correct_option": "D",
        "explanation": "Trigger side effects are undone when downstream payment validation fails."
      }
    ]
  },
  {
    "id": "MCQ-152",
    "title": "Role-Based Security & Privilege Delegation #1",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 46",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 126)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 126)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 126)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 126)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-153",
    "title": "Role-Based Security & Privilege Delegation #2",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 47",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 127)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 127)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 127)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 127)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-154",
    "title": "Role-Based Security & Privilege Delegation #3",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 48",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 128)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 128)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 128)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 128)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-155",
    "title": "Role-Based Security & Privilege Delegation #4",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 49",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 129)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 129)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 129)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 129)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-156",
    "title": "Role-Based Security & Privilege Delegation #5",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 50",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 130)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 130)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 130)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 130)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-157",
    "title": "Role-Based Security & Privilege Delegation #6",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 51",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 131)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 131)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 131)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 131)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-158",
    "title": "Role-Based Security & Privilege Delegation #7",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 52",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 132)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 132)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 132)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 132)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-159",
    "title": "Role-Based Security & Privilege Delegation #8",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 53",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 133)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 133)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 133)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 133)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-160",
    "title": "Role-Based Security & Privilege Delegation #9",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 54",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 134)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 134)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 134)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 134)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-161",
    "title": "Role-Based Security & Privilege Delegation #10",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 55",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 135)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 135)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 135)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 135)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-162",
    "title": "Role-Based Security & Privilege Delegation #11",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 56",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 136)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 136)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 136)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 136)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-163",
    "title": "Role-Based Security & Privilege Delegation #12",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 2 | Question: 57",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 137)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 137)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 137)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 137)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-164",
    "title": "Role-Based Security & Privilege Delegation #13",
    "topic": "Database Security & Access Control (RBAC/DCL)",
    "subtopic": "Role Hierarchies and Least Privilege",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 2 | Question: 58",
    "prompt": "In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 138)?",
    "options": [
      "A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty",
      "B. Because superuser accounts cannot execute SELECT queries",
      "C. To reduce the cost of database software licenses",
      "D. Because operating systems forbid root users"
    ],
    "correct_option": "A",
    "explanation": "The Principle of Least Privilege requires that users/roles possess only the minimal privileges necessary to perform their legitimate tasks, preventing privilege escalation and data leakage.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In clinical databases, why are nurses granted rights to record vitals but strictly denied privileges to ALTER TABLE or DROP TABLE (Case 138)?",
        "options": [
          "A. Because nurses cannot use SQL commands",
          "B. Least privilege limits nurse roles to clinical charting, preventing catastrophic accidental schema damage",
          "C. Because vitals tables are immutable",
          "D. To force doctors to enter all vitals"
        ],
        "correct_option": "B",
        "explanation": "Least privilege ensures clinical staff cannot accidentally alter underlying database schemas."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "Why are bank tellers restricted from granting table privileges to other tellers (Case 138)?",
        "options": [
          "A. Because tellers share one username",
          "B. Because banking databases have no roles",
          "C. Separation of duties prevents tellers from escalating their own authorization levels without security officer approval",
          "D. To double transaction processing time"
        ],
        "correct_option": "C",
        "explanation": "Separation of duties prevents unauthorized privilege escalation in financial ledgers."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "Why are marketplace customer service representatives denied SELECT access to raw credit card CVVs (Case 138)?",
        "options": [
          "A. Because CVVs are stored in plaintext cookies",
          "B. To prevent shoppers from buying products",
          "C. Because customer service only uses email",
          "D. Least privilege and PCI-DSS compliance prohibit customer service from accessing raw payment credentials"
        ],
        "correct_option": "D",
        "explanation": "Least privilege restricts customer service from viewing sensitive payment credentials."
      }
    ]
  },
  {
    "id": "MCQ-165",
    "title": "Concurrency Serializability & Transaction Safety #1",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 49",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 139)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 139)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 139)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 139)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-166",
    "title": "Concurrency Serializability & Transaction Safety #2",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 50",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 140)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 140)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 140)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 140)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-167",
    "title": "Concurrency Serializability & Transaction Safety #3",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 3 | Question: 51",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 141)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 141)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 141)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 141)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-168",
    "title": "Concurrency Serializability & Transaction Safety #4",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 52",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 142)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 142)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 142)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 142)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-169",
    "title": "Concurrency Serializability & Transaction Safety #5",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 53",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 143)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 143)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 143)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 143)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-170",
    "title": "Concurrency Serializability & Transaction Safety #6",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 3 | Question: 54",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 144)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 144)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 144)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 144)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-171",
    "title": "Concurrency Serializability & Transaction Safety #7",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 55",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 145)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 145)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 145)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 145)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-172",
    "title": "Concurrency Serializability & Transaction Safety #8",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 56",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 146)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 146)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 146)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 146)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-173",
    "title": "Concurrency Serializability & Transaction Safety #9",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 3 | Question: 57",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 147)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 147)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 147)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 147)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-174",
    "title": "Concurrency Serializability & Transaction Safety #10",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 58",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 148)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 148)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 148)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 148)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-175",
    "title": "Concurrency Serializability & Transaction Safety #11",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 59",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 149)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 149)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 149)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 149)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-176",
    "title": "Concurrency Serializability & Transaction Safety #12",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Hard",
    "source": "UGC NET CSE | Part 3 | Question: 60",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 150)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 150)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 150)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 150)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-177",
    "title": "Concurrency Serializability & Transaction Safety #13",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 61",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 151)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 151)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 151)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 151)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  },
  {
    "id": "MCQ-178",
    "title": "Concurrency Serializability & Transaction Safety #14",
    "topic": "Transactions & Concurrency Control",
    "subtopic": "Serializability and Invariant Guarantees",
    "difficulty": "Medium",
    "source": "UGC NET CSE | Part 3 | Question: 62",
    "prompt": "In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 152)?",
    "options": [
      "A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit",
      "B. To eliminate the need for primary keys",
      "C. To allow transactions to run without acquiring locks",
      "D. Because serial schedules are inherently slower"
    ],
    "correct_option": "A",
    "explanation": "Rigorous 2PL aligns the logical serialization order with the physical commit order, ensuring external consistency and preventing anomalies in distributed consensus.",
    "variants": [
      {
        "variant_id": 1,
        "domain": "Healthcare & Clinical EMR",
        "prompt": "In emergency room monitoring, why must patient vital updates serialize in the exact order clinical decisions commit (Case 152)?",
        "options": [
          "A. To discharge patients automatically",
          "B. To ensure real-time clinical dashboards display chronological patient health progression without retroactive state inversions",
          "C. Because medical databases cannot rollback",
          "D. To save monitor battery life"
        ],
        "correct_option": "B",
        "explanation": "Rigorous serialization preserves chronological clinical truth across medical monitors."
      },
      {
        "variant_id": 2,
        "domain": "Core Banking & FinTech Settlement",
        "prompt": "In interbank wire settlement, why must transaction serialization align with physical commit time (Case 152)?",
        "options": [
          "A. To prevent foreign exchange fluctuations",
          "B. Because banks cannot calculate interest otherwise",
          "C. To ensure regulatory audit logs reflect true real-time ledger balance progression without out-of-order anomalies",
          "D. To eliminate bank databases"
        ],
        "correct_option": "C",
        "explanation": "Aligning serialization with commit time guarantees verifiable real-time financial audit trails."
      },
      {
        "variant_id": 3,
        "domain": "E-Commerce Flash Sale & Inventory",
        "prompt": "In flash sale inventory checkouts, why must order serialization match commit sequence (Case 152)?",
        "options": [
          "A. To charge shoppers double price",
          "B. To allow carts to hold items for 30 days",
          "C. Because products have no serial numbers",
          "D. To ensure the last remaining item is awarded to the shopper whose transaction committed first in physical time"
        ],
        "correct_option": "D",
        "explanation": "Strict commit-ordered serialization ensures fair inventory allocation during flash sales."
      }
    ]
  }
]
