# Competitive Exam DBMS Questions & Answer Key (No Explanation)

**Project**: RBAC-Simulator & AI DBMS Practice Lab
**Total Questions**: 178 Authentic Entrance Exam Questions
**Breakdown**: GATE CS/DA (50), ISRO Scientist/Engineer (21), NIELIT Scientist B (29), UGC-NET CS (78)

---

## Section 1: GATE Computer Science & Data Science Questions (MCQ-001 to MCQ-050)

---

### Question 1: [MCQ-001] B+ Tree Root Node Occupancy Relaxation Invariant
- **Exam Source**: GATE CSE 2024 Set 1 | Question: 21 (PYQs/CS124S5.pdf, Page 15)
- **Topic**: Indexing & Storage &bull; B+ Tree Node Occupancy Invariants
- **Difficulty**: Easy

**Question Statement**:
In a B+ tree of order p, the requirement of at least half-full (50%) node occupancy is relaxed for which one of the following cases?

**Options**:
- A. Only the root node
- B. All leaf nodes
- C. All internal nodes except the root
- D. Only the leftmost leaf node

**Correct Answer**: **Option A** (Only the root node)

---

### Question 2: [MCQ-002] First Normal Form (1NF) Composite Attribute Invariants
- **Exam Source**: GATE CSE 2024 Set 1 | Question: 22 (PYQs/CS124S5.pdf, Page 15)
- **Topic**: Normalization & Functional Dependencies &bull; First Normal Form Invariants
- **Difficulty**: Medium

**Question Statement**:
Which of the following statements about a relation R in first normal form (1NF) is TRUE?

**Options**:
- A. R can have a multi-valued attribute
- B. R can have a composite attribute
- C. All attributes in R must be part of some candidate key
- D. Every attribute in R must be atomic and non-divisible

**Correct Answer**: **Option D** (Every attribute in R must be atomic and non-divisible)

---

### Question 3: [MCQ-003] Armstrong Axioms and Functional Dependency Deduction
- **Exam Source**: GATE CSE 2024 Set 1 | Question: 44 (PYQs/CS124S5.pdf, Page 28)
- **Topic**: Functional Dependencies &bull; Inference Rules & Axioms
- **Difficulty**: Medium

**Question Statement**:
Let X, Y, Z be sets of attributes in a relational schema, and -> denote functional dependency. According to Armstrong's Axioms and sound inference rules, which of the following is always TRUE?

**Options**:
- A. If X -> Y and Y -> Z, then X -> Z (Transitivity)
- B. If X -> Y, then XZ -> YZ for any attribute set Z (Augmentation)
- C. If X -> Y and X -> Z, then X -> YZ (Union rule)
- D. All of the above (Transitivity, Augmentation, and Union rules are all sound)

**Correct Answer**: **Option D** (All of the above (Transitivity, Augmentation, and Union rules are all sound))

---

### Question 4: [MCQ-004] Relational Division and Subquery Tuple Cardinality
- **Exam Source**: GATE CSE 2025 Set 1 | Question: 39 (PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf, Page 39)
- **Topic**: SQL & Relational Algebra &bull; Relational Division & Universal Quantification
- **Difficulty**: Hard

**Question Statement**:
Consider two relations describing teams and players: Teams(tid, tname) and Players(pid, pname, tid). A query is designed to find all teams that have players registered for every position in a reference table Positions(pos_name). In relational algebra, which algebraic construct precisely captures this universal quantification condition?

**Options**:
- A. Natural Join (⨝)
- B. Relational Division (÷)
- C. Outer Union (⊎)
- D. Left Outer Join (⟕)

**Correct Answer**: **Option B** (Relational Division (÷))

---

### Question 5: [MCQ-005] Candidate Keys and BCNF Decomposition of Functional Schemas
- **Exam Source**: GATE CSE 2025 Set 1 | Question: 47 (PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf, Page 47)
- **Topic**: Normalization & Functional Dependencies &bull; BCNF Decomposition & Keys
- **Difficulty**: Medium

**Question Statement**:
Consider a relational schema Team(name, city, owner) with functional dependencies F = {name -> city, name -> owner}. Which one of the following statements is CORRECT regarding the schema?

**Options**:
- A. The candidate key is {name}, and the schema is in 3NF and BCNF
- B. The candidate key is {name, city}, and the schema violates 2NF
- C. The candidate key is {owner}, and the schema is in 1NF only
- D. The schema violates BCNF because owner is transitively dependent on city

**Correct Answer**: **Option A** (The candidate key is {name}, and the schema is in 3NF and BCNF)

---

### Question 6: [MCQ-006] Candidate Key Minimal Closure for Multi-Attribute Relational Schema
- **Exam Source**: GATE DA 2024 | Question: 17 (PYQs/DA_extracted/DA/DA2024.pdf, Page 16)
- **Topic**: Functional Dependencies & Keys &bull; Candidate Key Minimal Closure
- **Difficulty**: Hard

**Question Statement**:
Let R(A, B, C, D, E) be a relational schema with functional dependency set F = {A -> BC, CD -> E, B -> D, E -> A}. Which of the following is a candidate key for R?

**Options**:
- A. {A}
- B. {B}
- C. {C}
- D. {D}

**Correct Answer**: **Option A** ({A})

---

### Question 7: [MCQ-007] Foreign Key Invariants on Natural Join and Cartesian Product
- **Exam Source**: GATE DA 2024 | Question: 26 (PYQs/DA_extracted/DA/DA2024.pdf, Page 19)
- **Topic**: Relational Model &bull; Foreign Key & Join Invariants
- **Difficulty**: Medium

**Question Statement**:
Consider two relations r and s defined on schemas R(A, B) and S(A, C). A is the primary key of R, and A in S is a foreign key referencing R(A) with no NULL values. If r has m tuples and s has n tuples, what is the exact number of tuples in the natural join r ⨝ s?

**Options**:
- A. Exactly m tuples
- B. Exactly n tuples
- C. At most m * n tuples and at least 0 tuples
- D. Exactly m + n tuples

**Correct Answer**: **Option B** (Exactly n tuples)

---

### Question 8: [MCQ-008] B+ Tree Maximum Key and Pointer Capacity Calculations
- **Exam Source**: GATE DA 2024 | Question: 41 (PYQs/DA_extracted/DA/DA2024.pdf, Page 29)
- **Topic**: Indexing & Storage &bull; B+ Tree Fan-out & Leaf Nodes
- **Difficulty**: Medium

**Question Statement**:
Consider a B+ Tree where the maximum number of keys in each leaf node is 2 and the maximum number of child pointers in each internal node is 3. What is the maximum number of keys that can be stored in a B+ Tree of height 2 (where root is at height 0)?

**Options**:
- A. 6 keys
- B. 18 keys
- C. 27 keys
- D. 54 keys

**Correct Answer**: **Option B** (18 keys)

---

### Question 9: [MCQ-009] SQL Correlated Subquery and Group By Aggregate Evaluation
- **Exam Source**: GATE DA 2024 | Question: 56 (PYQs/DA_extracted/DA/DA2024.pdf, Page 37)
- **Topic**: SQL & Query Processing &bull; Correlated Subqueries & Aggregates
- **Difficulty**: Hard

**Question Statement**:
Consider the relation Customer(cid, cname, rating, balance). Which of the following SQL queries retrieves the names of all customers whose balance is strictly greater than the average balance of all customers having the same credit rating?

**Options**:
- A. SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2)
- B. SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2 GROUP BY C2.rating)
- C. SELECT C1.cname FROM Customer C1 WHERE C1.balance > AVG(C1.balance)
- D. SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2 WHERE C2.rating = C1.rating)

**Correct Answer**: **Option D** (SELECT C1.cname FROM Customer C1 WHERE C1.balance > (SELECT AVG(C2.balance) FROM Customer C2 WHERE C2.rating = C1.rating))

---

### Question 10: [MCQ-010] Natural Join and Projection Cardinality on Three Relational Tables
- **Exam Source**: GATE DA 2025 | Question: 17 (PYQs/DA_extracted/DA/DA2025.pdf, Page 12)
- **Topic**: Relational Algebra &bull; Natural Join Cardinality
- **Difficulty**: Medium

**Question Statement**:
Consider three relations: Car(model, year, serial, color), Make(maker, model), and Own(owner, serial), where serial is the primary key of Car and Own(serial) is a foreign key referencing Car. What is the effect of the relational algebra expression: π_maker(Make ⨝ (Car ⨝ Own))?

**Options**:
- A. Names of all car makers who produce yellow cars
- B. Names of all car owners who own cars of every year
- C. Names of all car makers whose cars are currently owned by at least one owner
- D. Total count of car models registered in the database

**Correct Answer**: **Option C** (Names of all car makers whose cars are currently owned by at least one owner)

---

### Question 11: [MCQ-011] Referential Integrity Cascading Deletions on Foreign Keys
- **Exam Source**: GATE DA 2025 | Question: 56 (PYQs/DA_extracted/DA/DA2025.pdf, Page 30)
- **Topic**: Relational Model & Integrity Constraints &bull; Foreign Key ON DELETE CASCADE
- **Difficulty**: Medium

**Question Statement**:
Consider two relations Person(aadhaar PRIMARY KEY, name) and Customer(email PRIMARY KEY, name, phone, aadhaar FOREIGN KEY REFERENCES Person(aadhaar) ON DELETE CASCADE). If a tuple is deleted from Person, what happens in Customer?

**Options**:
- A. Deletion is rejected and aborted by the database engine
- B. All tuples in Customer referencing the deleted aadhaar are set to NULL
- C. All tuples in Customer referencing the deleted aadhaar are automatically deleted
- D. Only the first matching tuple in Customer is deleted

**Correct Answer**: **Option C** (All tuples in Customer referencing the deleted aadhaar are automatically deleted)

---

### Question 12: [MCQ-012] Candidate Key Derivation from Functional Dependencies
- **Exam Source**: GATE DA 2025 | Question: 57 (PYQs/DA_extracted/DA/DA2025.pdf, Page 31)
- **Topic**: Functional Dependencies &bull; Candidate Key Computation
- **Difficulty**: Medium

**Question Statement**:
Consider relation R(A, B, C, D, E, F, G) with functional dependencies: A -> BCEF, E -> DG, and BC -> A. Which of the following sets contains all candidate keys of R?

**Options**:
- A. {A, BC}
- B. {A, E}
- C. {BC, DG}
- D. {A, BC, E}

**Correct Answer**: **Option A** ({A, BC})

---

### Question 13: [MCQ-013] Minimal Candidate Key Identification with Extraneous Attributes
- **Exam Source**: GATE DA 2026 | Question: 17 (PYQs/DA_extracted/DA/DA2026.pdf, Page 12)
- **Topic**: Functional Dependencies &bull; Candidate Key Computation
- **Difficulty**: Medium

**Question Statement**:
Let R(A, B, C, D, E) be a relational schema with functional dependencies F = {A -> BC, CD -> E, E -> A}. Which of the following statements is correct?

**Options**:
- A. AD, ED and CD are the only candidate keys of R
- B. AD and ED are the only candidate keys of R
- C. A, E and CD are the only candidate keys of R
- D. CD is the only candidate key of R

**Correct Answer**: **Option A** (AD, ED and CD are the only candidate keys of R)

---

### Question 14: [MCQ-014] Operations Preserving Referential Integrity Invariants
- **Exam Source**: GATE DA 2026 | Question: 26 (PYQs/DA_extracted/DA/DA2026.pdf, Page 18)
- **Topic**: Relational Model & Integrity Constraints &bull; Foreign Key Modification Safety
- **Difficulty**: Easy

**Question Statement**:
Consider relations r and s on schemas R(A, B) and S(E, C) where A is the primary key of R and E is a foreign key of S referencing A in R. Which pair of operations will NEVER violate the foreign key constraint?

**Options**:
- A. Inserting records into relation r, and deleting records from relation s
- B. Deleting records from relation r, and inserting records into relation s
- C. Updating attribute A in relation r, and updating attribute E in relation s
- D. Deleting records from relation r, and deleting records from relation s

**Correct Answer**: **Option A** (Inserting records into relation r, and deleting records from relation s)

---

### Question 15: [MCQ-015] B+ Tree Node Split and Key Promotion on Insertion
- **Exam Source**: GATE DA 2026 | Question: 41 (PYQs/DA_extracted/DA/DA2026.pdf, Page 26)
- **Topic**: Indexing & Storage &bull; B+ Tree Insertion and Splitting
- **Difficulty**: Hard

**Question Statement**:
Consider a B+ Tree where leaf nodes hold at most 2 keys and internal nodes hold at most 3 pointers (order 3). Initially, the tree contains leaf [1, 2] and [5, 8] with root containing key 5. Upon inserting key 3 into the leftmost leaf [1, 2], the leaf overflows to [1, 2, 3] and splits. What key(s) are stored in the root node after rebalancing?

**Options**:
- A. 3, 5
- B. 5
- C. 2, 5
- D. 3

**Correct Answer**: **Option A** (3, 5)

---

### Question 16: [MCQ-016] Natural Join Tuple Cardinality Across Three Relations
- **Exam Source**: GATE DA 2026 | Question: 42 (PYQs/DA_extracted/DA/DA2026.pdf, Page 27)
- **Topic**: Relational Algebra &bull; Multi-Table Natural Join
- **Difficulty**: Medium

**Question Statement**:
Consider relations X(P, Q, R), Y(P, Q, S), and Z(P, T). Suppose X has tuples {(1, 2, 'a'), (1, 3, 'b')}, Y has tuples {(1, 2, 'c'), (1, 4, 'd')}, and Z has tuples {(1, 'e'), (2, 'f')}. How many tuples are present in the natural join X ⨝ Y ⨝ Z?

**Options**:
- A. 1
- B. 2
- C. 0
- D. 4

**Correct Answer**: **Option A** (1)

---

### Question 17: [MCQ-017] SQL Correlated Subquery and Windowing for Group Cardinality
- **Exam Source**: GATE DA 2026 | Question: 51 (PYQs/DA_extracted/DA/DA2026.pdf, Page 34)
- **Topic**: SQL & Query Processing &bull; Group Size Aggregation via Subquery
- **Difficulty**: Medium

**Question Statement**:
Consider table Employee(EmpID PK, TeamID NOT NULL). To display each employee's EmpID alongside the size of their team (TeamSize), which of the following SQL queries is correct?

**Options**:
- A. SELECT EmpID, (SELECT COUNT(*) FROM Employee E2 WHERE E2.TeamID = E1.TeamID) AS TeamSize FROM Employee E1
- B. SELECT EmpID, COUNT(TeamID) AS TeamSize FROM Employee GROUP BY EmpID
- C. SELECT EmpID, COUNT(*) AS TeamSize FROM Employee GROUP BY TeamID
- D. SELECT EmpID, SUM(TeamID) AS TeamSize FROM Employee

**Correct Answer**: **Option A** (SELECT EmpID, (SELECT COUNT(*) FROM Employee E2 WHERE E2.TeamID = E1.TeamID) AS TeamSize FROM Employee E1)

---

### Question 18: [MCQ-018] Dependency Preservation in 3NF and BCNF Decompositions
- **Exam Source**: GATE CSE 2026 Set 1 | Question: 31 (PYQs/CS_extracted/CS/2026_CS1.pdf, Page 23)
- **Topic**: Normalization & Functional Dependencies &bull; Dependency Preservation & Normal Forms
- **Difficulty**: Medium

**Question Statement**:
In the context of relational database schema normalization, which of the following statements is ALWAYS TRUE?

**Options**:
- A. It is always possible to obtain a lossless-join, dependency-preserving decomposition into 3NF
- B. It is always possible to obtain a lossless-join, dependency-preserving decomposition into BCNF
- C. Any relation with only prime attributes is in BCNF
- D. Lossless join decomposition is not guaranteed for 3NF

**Correct Answer**: **Option A** (It is always possible to obtain a lossless-join, dependency-preserving decomposition into 3NF)

---

### Question 19: [MCQ-019] Tuple Relational Calculus Equivalence to Relational Algebra Join
- **Exam Source**: GATE CSE 2026 Set 1 | Question: 43 (PYQs/CS_extracted/CS/2026_CS1.pdf, Page 32)
- **Topic**: Relational Calculus &bull; TRC to Relational Algebra Translation
- **Difficulty**: Hard

**Question Statement**:
Consider relations R(P, Q) and S(X, Y). Let E = { ⟨u⟩ | ∃v ∃w ( ⟨u, v⟩ ∈ R ∧ ⟨v, w⟩ ∈ S ) } be a tuple relational calculus expression. Which relational algebra expression is equivalent to E?

**Options**:
- A. ∏_P ( R ⨝_{R.Q = S.X} S )
- B. ∏_P ( R ⨝_{R.P = S.X} S )
- C. ∏_Q ( R ⨝_{R.Q = S.Y} S )
- D. ∏_X ( R ⨝_{R.P = S.Y} S )

**Correct Answer**: **Option A** (∏_P ( R ⨝_{R.Q = S.X} S ))

---

### Question 20: [MCQ-020] Armstrong Axioms: Derivation of the Union Rule
- **Exam Source**: GATE CSE 2026 Set 2 | Question: 42 (PYQs/CS_extracted/CS/2026_CS2.pdf, Page 29)
- **Topic**: Functional Dependencies &bull; Inference Rules & Axioms
- **Difficulty**: Medium

**Question Statement**:
According to Armstrong's Axioms (Reflexivity, Augmentation, Transitivity), how is the Union Rule ('If X -> Y and X -> Z, then X -> YZ') formally derived?

**Options**:
- A. By augmenting X -> Y with X to get X -> XY, augmenting X -> Z with Y to get XY -> YZ, and applying Transitivity to yield X -> YZ
- B. By taking the intersection of attribute closures of Y and Z
- C. By applying Reflexivity directly on attribute set YZ
- D. By decomposing X into disjoint subsets and applying Augmentation

**Correct Answer**: **Option A** (By augmenting X -> Y with X to get X -> XY, augmenting X -> Z with Y to get XY -> YZ, and applying Transitivity to yield X -> YZ)

---

### Question 21: [MCQ-021] ACID Properties: Transaction Durability Definition
- **Exam Source**: GATE CSE 2024 Set 2 | Question: 19 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 14)
- **Topic**: Transaction Processing &bull; ACID Properties & Crash Recovery
- **Difficulty**: Easy

**Question Statement**:
Once the DBMS informs the user that a transaction has been successfully completed, its effects must persist even if the system crashes before all changes are reflected on disk. This property is called:

**Options**:
- A. Durability
- B. Atomicity
- C. Consistency
- D. Isolation

**Correct Answer**: **Option A** (Durability)

---

### Question 22: [MCQ-022] ER Modeling: Weak Entity Total Participation Invariant
- **Exam Source**: GATE CSE 2024 Set 2 | Question: 20 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 14)
- **Topic**: Relational Model & Integrity Constraints &bull; ER Modeling & Weak Entities
- **Difficulty**: Easy

**Question Statement**:
In the context of owner (identifying) and weak entity sets in the ER (Entity-Relationship) model, which one of the following statements is TRUE?

**Options**:
- A. The weak entity set MUST have total participation in the identifying relationship
- B. The owner entity set MUST have total participation in the identifying relationship
- C. Both weak and owner entity sets MUST have total participation in the identifying relationship
- D. Neither weak nor owner entity set is required to have total participation

**Correct Answer**: **Option A** (The weak entity set MUST have total participation in the identifying relationship)

---

### Question 23: [MCQ-023] Two-Phase Locking (2PL) Protocol Phase Transition Invariant
- **Exam Source**: GATE CSE 2024 Set 2 | Question: 27 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 19)
- **Topic**: Concurrency Control &bull; Two-Phase Locking (2PL)
- **Difficulty**: Medium

**Question Statement**:
Which fundamental invariant defines the Two-Phase Locking (2PL) protocol?

**Options**:
- A. Once a lock is released on any data item by a transaction, no new locks can be acquired by that transaction
- B. All locks must be released before any data item can be updated
- C. Shared locks cannot be converted to exclusive locks under any circumstances
- D. A transaction releases all its locks at the exact moment it starts execution

**Correct Answer**: **Option A** (Once a lock is released on any data item by a transaction, no new locks can be acquired by that transaction)

---

### Question 24: [MCQ-024] Relational Algebra Cross Products for At-Least-K Cardinality
- **Exam Source**: GATE CSE 2024 Set 2 | Question: 45 (PYQs/CS_extracted/CS/2024_CS2.pdf, Page 31)
- **Topic**: Relational Algebra &bull; Cross Product Count for Minimum Cardinality
- **Difficulty**: Medium

**Question Statement**:
Consider the relation Person(pid, city), where pid is a unique identifier. Using only selection, projection, cross product, and rename, what is the minimum number of cross product operations required to find all cities where at least 3 distinct persons reside?

**Options**:
- A. 2
- B. 1
- C. 3
- D. 4

**Correct Answer**: **Option A** (2)

---

### Question 25: [MCQ-025] Relational Algebra Set Difference for Referential Inclusion
- **Exam Source**: GATE DA 2024 | Question: 26 (PYQs/DA_extracted/DA/DA2024.pdf, Page 16)
- **Topic**: Relational Algebra &bull; Set Difference for Universal Containment
- **Difficulty**: Medium

**Question Statement**:
Consider relations Defender(name, ...), Forward(name, ...), and Team(name, ...). Which relational algebra expression checks that every name occurring in Team appears in either Defender or Forward (where ∅ denotes the empty set)?

**Options**:
- A. ∏_name(Team) ∖ ( ∏_name(Defender) ∪ ∏_name(Forward) ) = ∅
- B. ∏_name(Team) ∖ ( ∏_name(Defender) ∩ ∏_name(Forward) ) = ∅
- C. ( ∏_name(Defender) ∪ ∏_name(Forward) ) ∖ ∏_name(Team) = ∅
- D. ( ∏_name(Defender) ∩ ∏_name(Forward) ) ∖ ∏_name(Team) = ∅

**Correct Answer**: **Option A** (∏_name(Team) ∖ ( ∏_name(Defender) ∪ ∏_name(Forward) ) = ∅)

---

### Question 26: [MCQ-026] Functional Dependency Derivation from Attribute Closure
- **Exam Source**: GATE DA 2024 | Question: 46 (PYQs/DA_extracted/DA/DA2024.pdf, Page 29)
- **Topic**: Functional Dependencies &bull; Attribute Closure and Derivability
- **Difficulty**: Medium

**Question Statement**:
Given relational schema R = (U, V, W, X, Y, Z) and functional dependencies F = {U -> V, U -> W, WX -> Y, WX -> Z, V -> X}. Which of the following functional dependencies can be derived from F?

**Options**:
- A. VW -> YZ
- B. VW -> U
- C. X -> YZ
- D. W -> Y

**Correct Answer**: **Option A** (VW -> YZ)

---

### Question 27: [MCQ-027] Cascading Rollback on Abort Due to Dirty Reads
- **Exam Source**: GATE CSE 2025 Set 1 | Question: 15 (PYQs/GATE-CS-2025-Set-1-Master-Question-Paper.pdf, Page 15)
- **Topic**: Concurrency Control &bull; Cascading Rollback & Dirty Reads
- **Difficulty**: Medium

**Question Statement**:
Consider schedule S of three transactions: R1(X) W1(Y) R2(X) R2(Y) R3(Y) ABORT(T1). If transaction T1 aborts, which other transaction(s) must undergo cascading rollback?

**Options**:
- A. Both T2 and T3
- B. Only T2
- C. Only T3
- D. Neither T2 nor T3

**Correct Answer**: **Option A** (Both T2 and T3)

---

### Question 28: [MCQ-028] Relational Schema Arity (Degree) Definition
- **Exam Source**: GATE CSE 2023 | Question: 16 (PYQs/CS_extracted/CS/2023_CS.pdf, Page 13)
- **Topic**: Relational Model & Integrity Constraints &bull; Schema Arity vs Relation Cardinality
- **Difficulty**: Easy

**Question Statement**:
Which of the following refers to the degree (or arity) of a relation in relational database systems?

**Options**:
- A. Number of attributes of its relation schema
- B. Number of tuples stored in the relation instance
- C. Total number of data entries across all cells
- D. Number of candidate keys defined on the relation

**Correct Answer**: **Option A** (Number of attributes of its relation schema)

---

### Question 29: [MCQ-029] Relational Division Formal Algebraic Expression
- **Exam Source**: GATE CSE 2022 | Question: 25 (PYQs/CS_extracted/CS/2022_CS.pdf, Page 20)
- **Topic**: Relational Algebra &bull; Relational Division Implementation
- **Difficulty**: Hard

**Question Statement**:
Consider relations Employee(eId, Name), Brand(bId, bName), and Own(eId, bId). Which relational algebra expression correctly returns the set of eIds of employees who own ALL the brands?

**Options**:
- A. ∏_eId (Own) − ∏_eId ( ( ∏_eId (Own) × ∏_bId (Brand) ) − Own )
- B. ∏_eId (Own) − ∏_eId ( ∏_eId (Own) × ∏_bId (Brand) )
- C. ∏_eId (Own) ∪ ∏_eId ( ( ∏_eId (Own) × ∏_bId (Brand) ) − Own )
- D. ∏_eId ( ∏_eId (Own) × ∏_bId (Brand) )

**Correct Answer**: **Option A** (∏_eId (Own) − ∏_eId ( ( ∏_eId (Own) × ∏_bId (Brand) ) − Own ))

---

### Question 30: [MCQ-030] Identification of 3NF Schemas Violating BCNF
- **Exam Source**: GATE CSE 2018 | Question: 42 (PYQs/CS_extracted/CS/2018_CS.pdf, Page 18)
- **Topic**: Normalization & Functional Dependencies &bull; 3NF vs BCNF Distinction
- **Difficulty**: Medium

**Question Statement**:
Consider relation Schema II: Registration(rollno, courseid, email) with functional dependencies: { (rollno, courseid) -> email, email -> rollno }. What is the highest normal form satisfied by this schema?

**Options**:
- A. 3NF (satisfies 3NF but violates BCNF)
- B. BCNF
- C. 2NF only
- D. 1NF only

**Correct Answer**: **Option A** (3NF (satisfies 3NF but violates BCNF))

---

### Question 31: [MCQ-031] Superkey Identification from Primary Key Invariant
- **Exam Source**: GATE CSE 2016 Set 1 | Question: 21 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 10)
- **Topic**: Functional Dependencies &bull; Superkeys vs Candidate Keys
- **Difficulty**: Easy

**Question Statement**:
Which of the following is NOT a superkey in a relational schema with attributes V, W, X, Y, Z and primary key VY?

**Options**:
- A. VWXZ
- B. VXYZ
- C. VWXY
- D. VWXYZ

**Correct Answer**: **Option A** (VWXZ)

---

### Question 32: [MCQ-032] ACID Properties: Exclusion of Operational Properties
- **Exam Source**: GATE CSE 2016 Set 1 | Question: 22 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 10)
- **Topic**: Transaction Processing &bull; ACID Properties of Transactions
- **Difficulty**: Easy

**Question Statement**:
Which one of the following is NOT a part of the ACID properties of database transactions?

**Options**:
- A. Deadlock-freedom
- B. Atomicity
- C. Consistency
- D. Isolation

**Correct Answer**: **Option A** (Deadlock-freedom)

---

### Question 33: [MCQ-033] Second Normal Form (2NF) Partial Dependency Elimination
- **Exam Source**: GATE CSE 2016 Set 1 | Question: 23 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 11)
- **Topic**: Normalization & Functional Dependencies &bull; Second Normal Form (2NF)
- **Difficulty**: Medium

**Question Statement**:
A relation R(VOLUME, NUMBER, STARTPAGE, ENDPAGE, TITLE, YEAR, PRICE) has primary key (VOLUME, NUMBER, STARTPAGE, ENDPAGE) and dependency (VOLUME, NUMBER) -> YEAR. When decomposed into R1(VOLUME, NUMBER, STARTPAGE, ENDPAGE, TITLE, PRICE) and R2(VOLUME, NUMBER, YEAR), what is the weakest normal form satisfied by the new database that the old one violated?

**Options**:
- A. 2NF
- B. 1NF
- C. 3NF
- D. BCNF

**Correct Answer**: **Option A** (2NF)

---

### Question 34: [MCQ-034] Strict Two-Phase Locking with Resource Ordering Guarantees
- **Exam Source**: GATE CSE 2016 Set 1 | Question: 51 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 19)
- **Topic**: Concurrency Control &bull; Lock Ordering and Deadlock Prevention
- **Difficulty**: Medium

**Question Statement**:
Consider a concurrency protocol where every transaction T: (1) acquires exclusive locks on all required data objects in strictly increasing order of their memory addresses, (2) performs all read/write operations, and (3) releases all locks at termination. What guarantees does this protocol provide?

**Options**:
- A. Guarantees both serializability and deadlock-freedom
- B. Guarantees serializability but not deadlock-freedom
- C. Guarantees deadlock-freedom but not serializability
- D. Guarantees neither serializability nor deadlock-freedom

**Correct Answer**: **Option A** (Guarantees both serializability and deadlock-freedom)

---

### Question 35: [MCQ-035] B+ Tree Balanced Property Definition
- **Exam Source**: GATE CSE 2016 Set 2 | Question: 21 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 31)
- **Topic**: Indexing & Storage &bull; B+ Tree Balanced Invariants
- **Difficulty**: Easy

**Question Statement**:
B+ Trees are considered BALANCED because:

**Options**:
- A. The lengths of the paths from the root to all leaf nodes are all equal
- B. The lengths of the paths from the root to all leaf nodes differ by at most 1
- C. The number of keys in any two leaf nodes is identical
- D. The number of child pointers in all internal nodes is identical

**Correct Answer**: **Option A** (The lengths of the paths from the root to all leaf nodes are all equal)

---

### Question 36: [MCQ-036] Precedence Graph Topological Ordering for Equivalent Serial Schedule
- **Exam Source**: GATE CSE 2016 Set 2 | Question: 22 (PYQs/CS_extracted/CS/2016_CS.pdf, Page 31)
- **Topic**: Concurrency Control &bull; Precedence Graph & Conflict Serializability
- **Difficulty**: Easy

**Question Statement**:
Suppose a database schedule S involves transactions T1, ..., Tn with an acyclic precedence graph (conflict serializable). Which vertex ordering of the precedence graph is guaranteed to produce an equivalent serial schedule?

**Options**:
- A. Topological order
- B. Depth-first order
- C. Breadth-first order
- D. Ascending order of transaction IDs

**Correct Answer**: **Option A** (Topological order)

---

### Question 37: [MCQ-037] Candidate Key Derivation from Multi-Attribute Functional Dependencies
- **Exam Source**: GATE CSE 2014 Set 1 | Question: 21 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 12)
- **Topic**: Functional Dependencies &bull; Candidate Key Computation
- **Difficulty**: Medium

**Question Statement**:
Consider relation scheme R = (E, F, G, H, I, J, K, L, M, N) and functional dependencies F = { {E, F} -> {G}, {F} -> {I, J}, {E, H} -> {K, L}, {K} -> {M}, {L} -> {N} }. What is the candidate key for R?

**Options**:
- A. {E, F, H}
- B. {E, F}
- C. {E, F, H, K, L}
- D. {E}

**Correct Answer**: **Option A** ({E, F, H})

---

### Question 38: [MCQ-038] Foreign Key SQL Constraints and Check Assertion Validity
- **Exam Source**: GATE CSE 2014 Set 1 | Question: 22 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 12)
- **Topic**: Relational Model & Integrity Constraints &bull; Foreign Key Definition & Check Constraints
- **Difficulty**: Medium

**Question Statement**:
Consider the statements:
S1: A foreign key declaration can always be replaced by an equivalent CHECK constraint in standard SQL.
S2: Given table R(a, b, c) where (a, b) together form the primary key, 'FOREIGN KEY (a) REFERENCES R' is a valid table definition.
Which one of the following is CORRECT?

**Options**:
- A. Both S1 and S2 are FALSE
- B. S1 is TRUE and S2 is FALSE
- C. S1 is FALSE and S2 is TRUE
- D. Both S1 and S2 are TRUE

**Correct Answer**: **Option A** (Both S1 and S2 are FALSE)

---

### Question 39: [MCQ-039] Conflict Serializability Testing on Concurrent Schedules
- **Exam Source**: GATE CSE 2014 Set 1 | Question: 29 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 14)
- **Topic**: Concurrency Control &bull; Precedence Graph Cycle Detection
- **Difficulty**: Medium

**Question Statement**:
Consider four schedules of three transactions operating on data item x. Which one of them is conflict serializable?

**Options**:
- A. r2(x); w2(x); r3(x); r1(x); w1(x)
- B. r1(x); r2(x); w1(x); r3(x); w2(x)
- C. r2(x); r1(x); w2(x); r3(x); w1(x)
- D. r3(x); r2(x); r1(x); w2(x); w1(x)

**Correct Answer**: **Option A** (r2(x); w2(x); r3(x); r1(x); w1(x))

---

### Question 40: [MCQ-040] Minimal Cover and Two-Attribute Relation Normal Form Invariants
- **Exam Source**: GATE CSE 2014 Set 1 | Question: 30 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 14)
- **Topic**: Functional Dependencies &bull; Minimal Cover & Binary Relation Normal Form
- **Difficulty**: Medium

**Question Statement**:
Consider two statements:
S1: Every relational table with two single-valued attributes is in 1NF, 2NF, 3NF, and BCNF.
S2: { AB -> C, D -> E, E -> C } is a minimal cover for { AB -> C, D -> E, AB -> E, E -> C }.
Which one of the following is CORRECT?

**Options**:
- A. S1 is TRUE and S2 is FALSE
- B. Both S1 and S2 are TRUE
- C. S1 is FALSE and S2 is TRUE
- D. Both S1 and S2 are FALSE

**Correct Answer**: **Option A** (S1 is TRUE and S2 is FALSE)

---

### Question 41: [MCQ-041] SQL Pairwise Comparison Subquery with GROUP BY and JOIN
- **Exam Source**: GATE CSE 2014 Set 1 | Question: 54 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 21)
- **Topic**: SQL & Query Processing &bull; Pairwise Subqueries & Join Semantics
- **Difficulty**: Hard

**Question Statement**:
Consider tables employees(emp_id, first_name, last_name, hire_date, dept_id, salary) and departments(dept_id, dept_name, manager_id, location_id). To display the last names and hire dates of all latest hires in their departments in location 1700, the following query is executed:
SELECT last_name, hire_date FROM employees WHERE (dept_id, hire_date) IN (SELECT dept_id, MAX(hire_date) FROM employees JOIN departments USING(dept_id) WHERE location_id = 1700 GROUP BY dept_id);
What is the outcome?

**Options**:
- A. It executes and gives the correct result
- B. It executes but does not give the correct result
- C. It generates an error because pairwise comparison is not allowed
- D. It generates an error because GROUP BY cannot be used in a subquery

**Correct Answer**: **Option A** (It executes and gives the correct result)

---

### Question 42: [MCQ-042] SQL Subquery Multiplicity and Duplicate Preservation
- **Exam Source**: GATE CSE 2014 Set 2 | Question: 54 (PYQs/CS_extracted/CS/2014_CS.pdf, Page 43)
- **Topic**: SQL & Query Processing &bull; Subquery Equivalence & Multiset Semantics
- **Difficulty**: Medium

**Question Statement**:
SQL operates under multiset (bag) semantics allowing duplicate tuples. Which of the following queries ALWAYS produces the exact same answer (including tuple multiplicity) as:
SELECT * FROM R WHERE a IN (SELECT S.a FROM S)?

**Options**:
- A. SELECT R.* FROM R, (SELECT DISTINCT a FROM S) AS S1 WHERE R.a = S1.a
- B. SELECT R.* FROM R, S WHERE R.a = S.a
- C. SELECT DISTINCT R.* FROM R, S WHERE R.a = S.a
- D. SELECT R.* FROM R, S WHERE R.a = S.a AND is unique R

**Correct Answer**: **Option A** (SELECT R.* FROM R, (SELECT DISTINCT a FROM S) AS S1 WHERE R.a = S1.a)

---

### Question 43: [MCQ-043] Clustered Index Physical Data File Organization
- **Exam Source**: GATE CSE 2013 | Question: 15 (PYQs/CS_extracted/CS/2013_CS.pdf, Page 5)
- **Topic**: Indexing & Storage &bull; Clustered vs Unclustered Indexing
- **Difficulty**: Easy

**Question Statement**:
An index is defined as a clustered index if:

**Options**:
- A. The data records of the file are physically organized in the same order as the data entries of the index
- B. It is created on a set of fields that form a candidate key
- C. It is created on a set of fields that include the primary key
- D. The data records of the file are organized in an order different from the index entries

**Correct Answer**: **Option A** (The data records of the file are physically organized in the same order as the data entries of the index)

---

### Question 44: [MCQ-044] Relational Query Equivalence Across SQL, RA, TRC, and DRC
- **Exam Source**: GATE CSE 2013 | Question: 35 (PYQs/CS_extracted/CS/2013_CS.pdf, Page 9)
- **Topic**: Relational Algebra &bull; Formal Query Language Equivalence
- **Difficulty**: Hard

**Question Statement**:
Consider schema Students(rollno, sname), Courses(courseno, cname), Registration(rollno, courseno, percent). Query: 'Find distinct names of all students scoring > 90% in course 107'.
I. SQL: SELECT DISTINCT S.sname FROM Students S, Registration R WHERE R.rollno=S.rollno AND R.courseno=107 AND R.percent > 90
II. Relational Algebra: ∏_sname ( σ_{courseno=107 ∧ percent>90} (Registration ⨝ Students) )
III. TRC: { T | ∃S∈Students ∃R∈Registration ( S.rollno=R.rollno ∧ R.courseno=107 ∧ R.percent>90 ∧ T.sname=S.sname ) }
IV. DRC: { ⟨SN⟩ | ∃SR ∃RP ( ⟨SR, SN⟩∈Students ∧ ⟨SR, 107, RP⟩∈Registration ∧ RP>90 ) }
Which of these queries correctly express the requirement?

**Options**:
- A. I, II, III, and IV
- B. I, II, and III only
- C. I, II, and IV only
- D. II, III, and IV only

**Correct Answer**: **Option A** (I, II, III, and IV)

---

### Question 45: [MCQ-045] Relational Normal Form Hierarchy: BCNF Subsumption of 3NF
- **Exam Source**: GATE CSE 2012 | Question: 2 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 2)
- **Topic**: Normalization & Functional Dependencies &bull; Normal Form Hierarchy & Containment
- **Difficulty**: Easy

**Question Statement**:
Which of the following statements regarding database normal forms is TRUE?

**Options**:
- A. Every relation in BCNF is also in 3NF
- B. Every relation in 3NF is also in BCNF
- C. A relation is in 3NF if every non-prime attribute is fully functionally dependent on every key
- D. No relation can be in both BCNF and 3NF simultaneously

**Correct Answer**: **Option A** (Every relation in BCNF is also in 3NF)

---

### Question 46: [MCQ-046] Relational Model Atomicity vs ER Multivalued Attributes
- **Exam Source**: GATE CSE 2012 | Question: 14 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 4)
- **Topic**: Relational Model & Integrity Constraints &bull; Relational Model Tuple Invariants
- **Difficulty**: Easy

**Question Statement**:
Given the basic ER and relational models, which of the following statements is INCORRECT?

**Options**:
- A. In a row of a relational table, an attribute can have more than one value
- B. An attribute of an entity in an ER model can have more than one value
- C. An attribute of an entity in an ER model can be composite
- D. In a row of a relational table, an attribute can have exactly one value or a NULL value

**Correct Answer**: **Option A** (In a row of a relational table, an attribute can have more than one value)

---

### Question 47: [MCQ-047] SQL HAVING Clause Without GROUP BY and Projection Invariants
- **Exam Source**: GATE CSE 2012 | Question: 15 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 4)
- **Topic**: SQL & Query Processing &bull; HAVING Clause and Projection Rules
- **Difficulty**: Medium

**Question Statement**:
Consider the following statements about an SQL query:
P: An SQL query can contain a HAVING clause even if it does not have a GROUP BY clause.
Q: An SQL query can contain a HAVING clause only if it has a GROUP BY clause.
R: All attributes used in the GROUP BY clause must appear in the SELECT clause.
S: Not all attributes used in the GROUP BY clause need to appear in the SELECT clause.
Which statements are TRUE?

**Options**:
- A. P and S
- B. P and R
- C. Q and R
- D. Q and S

**Correct Answer**: **Option A** (P and S)

---

### Question 48: [MCQ-048] Foreign Key Set Difference Invariant Under Referential Integrity
- **Exam Source**: GATE CSE 2012 | Question: 43 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 10)
- **Topic**: Relational Model & Integrity Constraints &bull; Foreign Key Inclusion Invariants
- **Difficulty**: Medium

**Question Statement**:
Suppose R1(A, B) and R2(C, D) are relation schemas, and r1, r2 are their instances. Attribute B in R1 is a foreign key referencing primary key C in R2. Assuming referential integrity is satisfied, which of the following is ALWAYS TRUE?

**Options**:
- A. ∏_B (r1) − ∏_C (r2) = ∅
- B. ∏_C (r2) − ∏_B (r1) = ∅
- C. ∏_B (r1) = ∏_C (r2)
- D. ∏_B (r1) − ∏_C (r2) ≠ ∅

**Correct Answer**: **Option A** (∏_B (r1) − ∏_C (r2) = ∅)

---

### Question 49: [MCQ-049] Relational Algebra Theta Join Cardinality with Disjunctive Predicate
- **Exam Source**: GATE CSE 2012 | Question: 50 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 14)
- **Topic**: Relational Algebra &bull; Theta Join & Disjunctive Conditions
- **Difficulty**: Hard

**Question Statement**:
Consider relations A(Id, Name, Age), B(Id, Name, Age), and C(Id, Phone, Area):
- A has tuples: (12, Arun, 60), (15, Shreya, 24), (99, Rohit, 11)
- B has tuples: (15, Shreya, 24), (25, Hari, 40), (98, Rohit, 20), (99, Rohit, 11)
- C has tuples: (10, 2200, 02), (99, 2100, 01)
How many tuples does the result of (A ∪ B) ⋈_{A.Id > 40 ∨ C.Id < 15} C contain?

**Options**:
- A. 7
- B. 4
- C. 5
- D. 9

**Correct Answer**: **Option A** (7)

---

### Question 50: [MCQ-050] SQL Subquery Evaluation with ALL Predicate on Empty Set
- **Exam Source**: GATE CSE 2012 | Question: 51 (PYQs/CS_extracted/CS/2012_CS.pdf, Page 14)
- **Topic**: SQL & Query Processing &bull; Quantified Comparison (ALL) with Empty Subqueries
- **Difficulty**: Medium

**Question Statement**:
Consider table A(Id, Name, Age) with 3 tuples: (12, 'Arun', 60), (15, 'Shreya', 24), (99, 'Rohit', 11), and table B(Id, Name, Age) containing tuples only for 'Shreya', 'Hari', and 'Rohit' (no row with Name = 'Arun'). How many tuples are returned by the query:
SELECT A.Id FROM A WHERE A.Age > ALL (SELECT B.Age FROM B WHERE B.Name = 'Arun');

**Options**:
- A. 3
- B. 0
- C. 1
- D. 4

**Correct Answer**: **Option A** (3)

---

## Section 2: ISRO Scientist/Engineer (Computer Science) Questions (MCQ-051 to MCQ-071)

---

### Question 51: [MCQ-051] Database Trigger Execution Semantics & Side Effects
- **Exam Source**: ISRO CSE 2016 | Question: 58
- **Topic**: Triggers & Active Databases &bull; Trigger Definition and Event Execution
- **Difficulty**: Easy

**Question Statement**:
Trigger is:

**Options**:
- A. Statement that enables to start any DBMS
- B. Statement that is executed by the user when debugging an application program
- C. The condition that the system tests for the validity of the database user
- D. Statement that is executed automatically by the system as a side effect of a modification of the database

**Correct Answer**: **Option D** (Statement that is executed automatically by the system as a side effect of a modification of the database)

---

### Question 52: [MCQ-052] Relational Object Access Control: GRANT & REVOKE
- **Exam Source**: ISRO CSE 2007 | Question: 47
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Data Control Language (DCL) Privileges
- **Difficulty**: Easy

**Question Statement**:
Which SQL commands are used to control access privileges over objects in a relational database?

**Options**:
- A. CASCADE & MVD
- B. GRANT & REVOKE
- C. QUE & QUIST
- D. COMMIT & ROLLBACK

**Correct Answer**: **Option B** (GRANT & REVOKE)

---

### Question 53: [MCQ-053] SQL Aggregate Functions and NULL Values
- **Exam Source**: ISRO CSE 2007 | Question: 48
- **Topic**: SQL Invariants & Declarative Constraints &bull; Aggregate Handling of NULL Tuples
- **Difficulty**: Easy

**Question Statement**:
Which of the following is a standard aggregate function in SQL, and how does it handle NULL values?

**Options**:
- A. SELECT; it returns NULL
- B. AVG; it ignores NULL values when computing the mean across tuples
- C. DISTINCT; it converts NULL to zero
- D. ORDER BY; it places NULLs at the beginning only

**Correct Answer**: **Option B** (AVG; it ignores NULL values when computing the mean across tuples)

---

### Question 54: [MCQ-054] Purpose of Foreign Key in Referential Integrity
- **Exam Source**: ISRO CSE 2009 | Question: 72
- **Topic**: Referential Integrity & Cascades &bull; Foreign Key Invariants and Parent Tables
- **Difficulty**: Easy

**Question Statement**:
The fundamental purpose of defining a 'Foreign Key' constraint in a relational database table is to ensure:

**Options**:
- A. Null integrity
- B. Referential integrity between related tables
- C. Domain integrity only
- D. Faster physical sorting on disk

**Correct Answer**: **Option B** (Referential integrity between related tables)

---

### Question 55: [MCQ-055] Natural Join Equivalence and Tuple Multiplication
- **Exam Source**: ISRO CSE 2017 | Question: 7
- **Topic**: SQL Invariants & Declarative Constraints &bull; Relational Natural Join Cardinality
- **Difficulty**: Medium

**Question Statement**:
Given relation Overtime_allowance(Employee, Department, OT_allowance). What is the output cardinality of: 'SELECT COUNT(*) FROM ((SELECT Employee, Department FROM Overtime_allowance) NATURAL JOIN (SELECT Department, OT_allowance FROM Overtime_allowance) AS T)' when multiple employees share the same department?

**Options**:
- A. It is always equal to the original number of rows in Overtime_allowance
- B. It can exceed the original count because tuples within the same department join in a Cartesian product across that department
- C. It always returns 0
- D. It produces a syntax error due to alias scoping

**Correct Answer**: **Option B** (It can exceed the original count because tuples within the same department join in a Cartesian product across that department)

---

### Question 56: [MCQ-056] Distinct Projection and Multiset Elimination
- **Exam Source**: ISRO CSE 2018 | Question: 40
- **Topic**: SQL Invariants & Declarative Constraints &bull; SELECT DISTINCT Cardinality Invariants
- **Difficulty**: Medium

**Question Statement**:
Given relations R(w, x) and S(y, z), the result of query 'SELECT DISTINCT w, x FROM R, S' is GUARANTEED to be identical to relation R if and only if:

**Options**:
- A. Relation S is completely empty
- B. Relation S contains at least one tuple, and R contains no duplicate tuples
- C. Relations R and S have identical schemas
- D. S has strictly more rows than R

**Correct Answer**: **Option B** (Relation S contains at least one tuple, and R contains no duplicate tuples)

---

### Question 57: [MCQ-057] Correlated Relational Division Querying
- **Exam Source**: ISRO CSE 2018 | Question: 42
- **Topic**: Relational Calculus & Relational Algebra &bull; Correlated NOT EXISTS Division Patterns
- **Difficulty**: Hard

**Question Statement**:
Given relations Students(Roll, Name), Courses(Course_No, Course_Name), Grades(Roll, Course_No, Grade). Which SQL query retrieves the names of all students who have enrolled in EVERY course?

**Options**:
- A. SELECT Name FROM Students S WHERE NOT EXISTS (SELECT Course_No FROM Courses C WHERE NOT EXISTS (SELECT * FROM Grades G WHERE G.Roll = S.Roll AND G.Course_No = C.Course_No))
- B. SELECT Name FROM Students NATURAL JOIN Grades NATURAL JOIN Courses
- C. SELECT Name FROM Students S WHERE (SELECT COUNT(*) FROM Grades G WHERE G.Roll = S.Roll) = 0
- D. SELECT Name FROM Students S WHERE S.Roll IN (SELECT Roll FROM Courses)

**Correct Answer**: **Option A** (SELECT Name FROM Students S WHERE NOT EXISTS (SELECT Course_No FROM Courses C WHERE NOT EXISTS (SELECT * FROM Grades G WHERE G.Roll = S.Roll AND G.Course_No = C.Course_No)))

---

### Question 58: [MCQ-058] ACID Properties: Fundamental Transaction Invariants
- **Exam Source**: ISRO CSE 2017 | Question: 6
- **Topic**: Transactions & Concurrency Control &bull; ACID Properties and Invariant Semantics
- **Difficulty**: Easy

**Question Statement**:
The ACID properties of database transactions stand for:

**Options**:
- A. Atomicity, consistency, isolation, database
- B. Atomicity, consistency, isolation, durability
- C. Atomicity, consistency, integrity, durability
- D. Authentication, consistency, isolation, durability

**Correct Answer**: **Option B** (Atomicity, consistency, isolation, durability)

---

### Question 59: [MCQ-059] Timestamp Ordering Protocol & Rollback Invariants
- **Exam Source**: ISRO CSE 2018 | Question: 55
- **Topic**: Transactions & Concurrency Control &bull; Timestamp Ordering and Thomas Write Rule
- **Difficulty**: Medium

**Question Statement**:
In the basic Timestamp Ordering (TO) concurrency control protocol, if transaction Ti attempts to execute read(X) when timestamp TS(Ti) < W_timestamp(X):

**Options**:
- A. Ti is allowed to read X immediately
- B. Ti is rolled back and restarted with a new timestamp because it attempted to read an overwritten value
- C. The write on X is reversed
- D. The system halts

**Correct Answer**: **Option B** (Ti is rolled back and restarted with a new timestamp because it attempted to read an overwritten value)

---

### Question 60: [MCQ-060] Raymond Tree-Based Distributed Mutual Exclusion
- **Exam Source**: ISRO CSE 2020 | Question: 22
- **Topic**: Transactions & Concurrency Control &bull; Distributed Mutual Exclusion Algorithms
- **Difficulty**: Hard

**Question Statement**:
Raymond's tree-based algorithm for distributed mutual exclusion organizes network nodes into a directed logical tree. What is its key operational property?

**Options**:
- A. It ensures no deadlock, but starvation may occur in rare unweighted topologies
- B. Messages are broadcast to all nodes simultaneously
- C. It requires O(N) message exchanges per critical section entry
- D. It uses physical synchronized clocks instead of logical tokens

**Correct Answer**: **Option A** (It ensures no deadlock, but starvation may occur in rare unweighted topologies)

---

### Question 61: [MCQ-061] 8085 Interrupt Triggering: Level vs Edge Sensitivity
- **Exam Source**: ISRO CSE 2008 | Question: 45
- **Topic**: Computer Architecture: Interrupts & Execution &bull; Microprocessor Interrupt Triggering Modes
- **Difficulty**: Medium

**Question Statement**:
In the 8085 microprocessor architecture, how is the TRAP non-maskable interrupt triggered?

**Options**:
- A. It is level-triggered only
- B. It is negative edge-triggered only
- C. It is both level and positive edge-sensitive (edge-and-level triggered) to prevent false triggering by noise
- D. It is software-triggered via the RST 0 instruction only

**Correct Answer**: **Option C** (It is both level and positive edge-sensitive (edge-and-level triggered) to prevent false triggering by noise)

---

### Question 62: [MCQ-062] Hardware Edge Triggering in Sequential Flip-Flops
- **Exam Source**: ISRO CSE 2007 | Question: 31
- **Topic**: Digital Logic: Flip-Flops & Hardware Triggers &bull; Clock Edge Triggering vs Level Latching
- **Difficulty**: Easy

**Question Statement**:
In digital sequential circuits, what is the primary operational advantage of an edge-triggered flip-flop over a level-sensitive latch?

**Options**:
- A. Edge-triggered circuits eliminate race-around conditions by sampling inputs only during clock transitions
- B. Latches consume zero dynamic power
- C. Edge-triggered flip-flops require no clock input
- D. Latches operate at higher gigahertz frequencies

**Correct Answer**: **Option A** (Edge-triggered circuits eliminate race-around conditions by sampling inputs only during clock transitions)

---

### Question 63: [MCQ-063] Network Medium Access Control (MAC) Sublayer Protocol
- **Exam Source**: ISRO CSE 2008 | Question: 4
- **Topic**: Computer Networks: Access Control & Security &bull; Medium Access Control and CSMA/CD
- **Difficulty**: Medium

**Question Statement**:
In the IEEE 802.3 Ethernet protocol, what is the core role of the Medium Access Control (MAC) sublayer in the Data Link Layer?

**Options**:
- A. Resolving contention and regulating transmission access over a shared physical channel using CSMA/CD
- B. Routing IP packets across autonomous systems via BGP
- C. Establishing end-to-end TCP byte streams
- D. Performing domain name translation

**Correct Answer**: **Option A** (Resolving contention and regulating transmission access over a shared physical channel using CSMA/CD)

---

### Question 64: [MCQ-064] Operating System Discretionary Access Control (DAC)
- **Exam Source**: ISRO CSE 2014 | Question: 39
- **Topic**: Operating Systems: Security & Access Control &bull; DAC Models and Permission Matrices
- **Difficulty**: Medium

**Question Statement**:
In Operating System security models, what defines Discretionary Access Control (DAC)?

**Options**:
- A. Access rights are determined strictly by system-wide mandatory security labels (e.g. Top Secret)
- B. The owner of an object has full discretion to grant or revoke access privileges (e.g. read/write/execute) to other users
- C. Access is granted based solely on the time of day
- D. All users possess identical root permissions

**Correct Answer**: **Option B** (The owner of an object has full discretion to grant or revoke access privileges (e.g. read/write/execute) to other users)

---

### Question 65: [MCQ-065] Kernel vs User Privilege Rings & Protection Domains
- **Exam Source**: ISRO CSE 2017 | Question: 70
- **Topic**: Operating Systems: Security & Access Control &bull; Privilege Levels and System Call Traps
- **Difficulty**: Medium

**Question Statement**:
Why do modern CPUs and operating systems enforce dual-mode operation (User Mode vs Kernel/Supervisor Mode)?

**Options**:
- A. To allow user applications to directly modify memory management page tables
- B. To protect operating system memory and hardware devices from unauthorized access or accidental corruption by user processes
- C. To eliminate the need for device drivers
- D. To double CPU clock frequency in user mode

**Correct Answer**: **Option B** (To protect operating system memory and hardware devices from unauthorized access or accidental corruption by user processes)

---

### Question 66: [MCQ-066] Two-Phase Commit Protocol in Distributed DBMS
- **Exam Source**: ISRO CSE 2023 | Question: 49
- **Topic**: Transactions & Concurrency Control &bull; Distributed Transactions and 2PC Protocol
- **Difficulty**: Hard

**Question Statement**:
In the Two-Phase Commit (2PC) protocol across distributed database nodes, what occurs if any single cohort participant votes 'NO' during Phase 1 (Prepare Phase)?

**Options**:
- A. The coordinator ignores the vote and commits anyway
- B. The coordinator broadcasts a global 'ABORT' message to all participants, ensuring atomicity is preserved
- C. The cohort voting NO is permanently disconnected from the cluster
- D. Phase 2 is skipped and data remains in a half-committed state

**Correct Answer**: **Option B** (The coordinator broadcasts a global 'ABORT' message to all participants, ensuring atomicity is preserved)

---

### Question 67: [MCQ-067] Checkpoint Recovery and Log Redo Pass
- **Exam Source**: ISRO CSE 2013 | Question: 23
- **Topic**: Transactions & Concurrency Control &bull; Checkpoint Recovery and Redo Pass
- **Difficulty**: Hard

**Question Statement**:
In database log-based recovery, what is the primary benefit of writing periodic 'CHECKPOINT' records to the log?

**Options**:
- A. It permanently prevents any future system crashes
- B. It bounds recovery time by guaranteeing that all log records prior to the checkpoint have already flushed their dirty buffer pages to disk
- C. It converts the database to read-only mode
- D. It eliminates the need for transaction undo operations

**Correct Answer**: **Option B** (It bounds recovery time by guaranteeing that all log records prior to the checkpoint have already flushed their dirty buffer pages to disk)

---

### Question 68: [MCQ-068] ER Modeling: Multivalued Attributes & Double Ellipse
- **Exam Source**: ISRO CSE 2017 | Question: 8
- **Topic**: Relational Model & Normalization &bull; Entity-Relationship Diagrams and Attribute Representations
- **Difficulty**: Easy

**Question Statement**:
In standard Entity-Relationship (ER) diagram notation (Peter Chen style), what does a 'double ellipse' represent?

**Options**:
- A. Key attribute
- B. Multivalued attribute
- C. Derived attribute
- D. Weak entity set

**Correct Answer**: **Option B** (Multivalued attribute)

---

### Question 69: [MCQ-069] Candidate Key Minimal Superkey Property
- **Exam Source**: ISRO CSE 2014 | Question: 42
- **Topic**: Relational Model & Normalization &bull; Candidate Key Invariants
- **Difficulty**: Medium

**Question Statement**:
What is the formal mathematical definition of a 'Candidate Key' in relational database theory?

**Options**:
- A. Any attribute that contains only integer values
- B. A minimal superkey (a set of attributes that uniquely identifies every tuple, with no proper subset being a superkey)
- C. Any column with an index built on it
- D. An attribute that references a primary key in another table

**Correct Answer**: **Option B** (A minimal superkey (a set of attributes that uniquely identifies every tuple, with no proper subset being a superkey))

---

### Question 70: [MCQ-070] B+ Tree Leaf Node Doubly Linked List Scanning
- **Exam Source**: ISRO CSE 2015 | Question: 18
- **Topic**: Physical Storage & Indexing &bull; B+ Tree Range Query Optimization
- **Difficulty**: Medium

**Question Statement**:
In database storage architectures, why is a B+ Tree overwhelmingly preferred over a standard B Tree for relational index structures?

**Options**:
- A. B+ Trees do not store keys in internal nodes
- B. All data pointers reside in leaf nodes, which are linked together in a sequential linked list enabling efficient range queries (e.g. BETWEEN X AND Y)
- C. B+ Trees require no rebalancing upon deletions
- D. B+ Trees consume zero memory in the buffer pool

**Correct Answer**: **Option B** (All data pointers reside in leaf nodes, which are linked together in a sequential linked list enabling efficient range queries (e.g. BETWEEN X AND Y))

---

### Question 71: [MCQ-071] Dense vs Sparse Secondary Indexing
- **Exam Source**: ISRO CSE 2017 | Question: 1
- **Topic**: Physical Storage & Indexing &bull; Dense and Sparse Index Structures
- **Difficulty**: Medium

**Question Statement**:
Which of the following statements about Dense and Sparse database indices is TRUE?

**Options**:
- A. A sparse index contains an index entry for every search key value in the data file
- B. A dense index contains an index record for every single search key value in the relation, whereas a sparse index contains records for only some search values
- C. Sparse indices can be built on un-ordered data files
- D. Dense indices cannot be used for primary keys

**Correct Answer**: **Option B** (A dense index contains an index record for every single search key value in the relation, whereas a sparse index contains records for only some search values)

---

## Section 3: NIELIT Scientist B & Technical Assistant Questions (MCQ-072 to MCQ-100)

---

### Question 72: [MCQ-072] Data Integrity Enforcement: Constraints vs Triggers
- **Exam Source**: NIELIT 2021 Dec Scientist B - Section B: 9
- **Topic**: Triggers & Active Databases &bull; Declarative Constraints vs Procedural Triggers
- **Difficulty**: Medium

**Question Statement**:
Specify, which of the following is the preferred method for enforcing data integrity in a relational database?

**Options**:
- A. Constraints
- B. Stored procedure
- C. Triggers
- D. Cursors

**Correct Answer**: **Option A** (Constraints)

---

### Question 73: [MCQ-073] Lock Synchronization in Concurrent Database Systems
- **Exam Source**: NIELIT 2016 MAR Scientist B - Section C: 34
- **Topic**: Transactions & Concurrency Control &bull; Global vs Local Locks
- **Difficulty**: Medium

**Question Statement**:
In distributed and multi-tier database systems, what is the primary function of Global Locks?

**Options**:
- A. Synchronize access to local resources exclusively within a single CPU core
- B. Synchronize access to global, shared resources across distributed database instances
- C. Are used to avoid local locks entirely
- D. Prevent all read access permanently across all nodes

**Correct Answer**: **Option B** (Synchronize access to global, shared resources across distributed database instances)

---

### Question 74: [MCQ-074] Irrecoverable Error Anomaly: Dirty Read followed by Uncommitted Write
- **Exam Source**: NIELIT 2022 April Scientist B | Section B | Question: 58
- **Topic**: Transactions & Concurrency Control &bull; Irrecoverable Schedules and Dirty Reads
- **Difficulty**: Hard

**Question Statement**:
Which of the following transaction execution scenarios leads to an IRRECOVERABLE error in a database system?

**Options**:
- A. A transaction writes a data item after it is read by an uncommitted transaction
- B. A transaction reads a data item after it is read by an uncommitted transaction
- C. A transaction reads a data item after it is written by a committed transaction
- D. A transaction reads a data item after it is written by an uncommitted transaction, and then commits before the writing transaction commits

**Correct Answer**: **Option D** (A transaction reads a data item after it is written by an uncommitted transaction, and then commits before the writing transaction commits)

---

### Question 75: [MCQ-075] Relational Lossless Join & Dependency Preservation
- **Exam Source**: NIELIT 2022 April Scientist B | Section B | Question: 49
- **Topic**: Relational Model & Normalization &bull; Decomposition Properties and Functional Dependencies
- **Difficulty**: Medium

**Question Statement**:
Let R(A, B, C, D) be a relational schema with functional dependencies F = {A -> B, B -> C, C -> D}. The decomposition of R into R1(A, B), R2(B, C), and R3(C, D):

**Options**:
- A. Gives a lossless join, and is dependency preserving
- B. Gives a lossless join, but is not dependency preserving
- C. Does not give a lossless join, but is dependency preserving
- D. Does not give a lossless join and is not dependency preserving

**Correct Answer**: **Option A** (Gives a lossless join, and is dependency preserving)

---

### Question 76: [MCQ-076] Highest Normal Form Determination under Functional Dependencies
- **Exam Source**: NIELIT 2022 April Scientist B | Section B | Question: 54
- **Topic**: Relational Model & Normalization &bull; Normal Form Hierarchy (1NF, 2NF, 3NF, BCNF)
- **Difficulty**: Hard

**Question Statement**:
Given relation R(Name, Course_No, Roll_No, Grade) with functional dependencies: {Name, Course_No -> Grade; Roll_No, Course_No -> Grade; Name -> Roll_No; Roll_No -> Name}. What is the HIGHEST normal form of R?

**Options**:
- A. 1NF
- B. 2NF
- C. 3NF
- D. BCNF

**Correct Answer**: **Option C** (3NF)

---

### Question 77: [MCQ-077] Self-Join and Unary Relationship Querying
- **Exam Source**: NIELIT 2017 July Scientist B (IT) - Section B: 55
- **Topic**: SQL Invariants & Declarative Constraints &bull; Self-Joins on Hierarchical Schemas
- **Difficulty**: Easy

**Question Statement**:
A table joined with itself in an SQL query is formally referred to as a:

**Options**:
- A. Natural Join
- B. Self Join
- C. Outer Join
- D. Equi Join

**Correct Answer**: **Option B** (Self Join)

---

### Question 78: [MCQ-078] Hash File Addressing & Record Location Transformation
- **Exam Source**: NIELIT Scientist B 2020 November: 103
- **Topic**: Physical Storage & Indexing &bull; Hash Addressing and Bucket Capacity
- **Difficulty**: Easy

**Question Statement**:
The physical storage organization where the location of a record is determined by a mathematical formula that transforms a search key into an address block is known as:

**Options**:
- A. B-Tree File
- B. Hashed File (Hash-based indexing)
- C. Indexed-Sequential File
- D. Heap File

**Correct Answer**: **Option B** (Hashed File (Hash-based indexing))

---

### Question 79: [MCQ-079] Role Permissions and Access Control Rights
- **Exam Source**: NIELIT 2017 OCT Scientific Assistant A - Section B: 54
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role-Based Access Control and Privilege Grants
- **Difficulty**: Medium

**Question Statement**:
In SQL Role-Based Access Control (RBAC), what is the primary architectural advantage of granting database privileges to 'ROLES' rather than directly to individual user accounts?

**Options**:
- A. It reduces disk storage consumption by 90%
- B. It simplifies privilege administration by decoupling user identities from access rights, allowing users to inherit permissions dynamically as their job roles change
- C. It disables all database logging to maximize throughput
- D. It eliminates the need for user passwords

**Correct Answer**: **Option B** (It simplifies privilege administration by decoupling user identities from access rights, allowing users to inherit permissions dynamically as their job roles change)

---

### Question 80: [MCQ-080] ER Diagram Weak Entity Representation
- **Exam Source**: NIELIT 2021 Dec Scientist A - Section B: 49
- **Topic**: Relational Model & Normalization &bull; Weak Entity Sets and Identifying Relationships
- **Difficulty**: Easy

**Question Statement**:
In an Entity-Relationship (ER) diagram, how are a 'Weak Entity Set' and its 'Identifying Relationship' visually represented?

**Options**:
- A. Single rectangle and single diamond
- B. Double rectangle (weak entity) and double diamond (identifying relationship)
- C. Double ellipse and single rectangle
- D. Dashed circle and underlined rectangle

**Correct Answer**: **Option B** (Double rectangle (weak entity) and double diamond (identifying relationship))

---

### Question 81: [MCQ-081] Referential Integrity Violation under Child Insertions
- **Exam Source**: NIELIT 2018 | Question: 49
- **Topic**: Referential Integrity & Cascades &bull; Foreign Key Insertion Invariants
- **Difficulty**: Medium

**Question Statement**:
In a database with Parent table P(P_ID PRIMARY KEY) and Child table C(C_ID PRIMARY KEY, P_ID REFERENCES P(P_ID)), which operation is GUARANTEED to cause a referential integrity violation if not properly checked?

**Options**:
- A. Inserting a new tuple into Parent table P
- B. Inserting a new tuple into Child table C with a P_ID value that does not exist in P
- C. Deleting a tuple from Child table C
- D. Querying Parent table P with a SELECT statement

**Correct Answer**: **Option B** (Inserting a new tuple into Child table C with a P_ID value that does not exist in P)

---

### Question 82: [MCQ-082] Foreign Key Constraints with ON DELETE CASCADE Semantics
- **Exam Source**: NIELIT 2021 Dec Scientist B - Section B: 10
- **Topic**: Referential Integrity & Cascades &bull; Cascade Deletion Execution Patterns
- **Difficulty**: Medium

**Question Statement**:
When defining a foreign key with 'ON DELETE CASCADE' in an SQL DDL statement, what action is executed by the DBMS engine when a referenced primary key tuple is deleted?

**Options**:
- A. The delete is rejected and an error is thrown
- B. All matching child tuples referencing that primary key are automatically deleted in the same transaction
- C. Foreign key columns in matching child rows are updated to 0
- D. The parent table is truncated

**Correct Answer**: **Option B** (All matching child tuples referencing that primary key are automatically deleted in the same transaction)

---

### Question 83: [MCQ-083] Entity Integrity Constraint: Non-Null Primary Keys
- **Exam Source**: NIELIT Scientific Assistant A 2020 November: 97
- **Topic**: SQL Invariants & Declarative Constraints &bull; Entity Integrity and Primary Key Non-Nullness
- **Difficulty**: Easy

**Question Statement**:
The 'Entity Integrity Constraint' in the relational model mandates that:

**Options**:
- A. Foreign key values must match primary key values
- B. No primary key attribute (or component of a composite primary key) may contain a NULL value
- C. Secondary indices must be dense
- D. Table names must be unique across the schema

**Correct Answer**: **Option B** (No primary key attribute (or component of a composite primary key) may contain a NULL value)

---

### Question 84: [MCQ-084] Relational Foreign Key Domain Compatibility
- **Exam Source**: NIELIT 2016 MAR Scientist B - Section C: 41
- **Topic**: Referential Integrity & Cascades &bull; Foreign Key Type Compatibility Rules
- **Difficulty**: Easy

**Question Statement**:
When establishing a foreign key relationship between Child(A) and Parent(B), what is the mandatory structural requirement on attributes A and B?

**Options**:
- A. Attribute A and Attribute B must have compatible data types and identical domains
- B. Attribute A must have twice the byte length of Attribute B
- C. Attributes A and B must share the same column name in both tables
- D. Both tables must reside on the same physical hard disk partition

**Correct Answer**: **Option A** (Attribute A and Attribute B must have compatible data types and identical domains)

---

### Question 85: [MCQ-085] Deadlock Avoidance: Wait-Die vs Wound-Wait Preemption
- **Exam Source**: NIELIT 2017 OCT Scientific Assistant A (IT): 72
- **Topic**: Transactions & Concurrency Control &bull; Non-preemptive vs Preemptive Timestamp Deadlock Schemes
- **Difficulty**: Medium

**Question Statement**:
Between the two timestamp-based deadlock prevention algorithms 'Wait-Die' and 'Wound-Wait', which one is classified as a NON-PREEMPTIVE scheme?

**Options**:
- A. Wound-Wait
- B. Wait-Die (because an older transaction is allowed to wait, and younger transactions die without preempting the lock holder)
- C. Both schemes are non-preemptive
- D. Neither scheme uses timestamps

**Correct Answer**: **Option B** (Wait-Die (because an older transaction is allowed to wait, and younger transactions die without preempting the lock holder))

---

### Question 86: [MCQ-086] ACID Atomicity Rollback Guarantee
- **Exam Source**: NIELIT 2021 Dec Scientist B - Section B: 78
- **Topic**: Transactions & Concurrency Control &bull; Transaction Abort and Rollback Invariants
- **Difficulty**: Easy

**Question Statement**:
When a database transaction aborts before reaching its commit point, the Atomicity property guarantees that:

**Options**:
- A. All changes made by the transaction are rolled back and undone, restoring the database to its pre-transaction state
- B. Only the last SQL query is reversed
- C. The database is restored to a random state
- D. The user's account is permanently deleted

**Correct Answer**: **Option A** (All changes made by the transaction are rolled back and undone, restoring the database to its pre-transaction state)

---

### Question 87: [MCQ-087] Stored Procedure Compilation & Pre-Compiled Execution Plans
- **Exam Source**: NIELIT 2018 | Question: 34
- **Topic**: Triggers & Active Databases &bull; Stored Procedures vs Dynamic SQL
- **Difficulty**: Medium

**Question Statement**:
What is a primary performance advantage of executing database operations via 'Stored Procedures' compared to sending ad-hoc dynamic SQL queries from an application?

**Options**:
- A. Stored procedures run without database transactions
- B. Stored procedures are parsed, optimized, and compiled once on the database server, reusing cached query execution plans and reducing network round-trips
- C. Stored procedures store all data in CPU cache permanently
- D. Stored procedures bypass SQL syntax checking

**Correct Answer**: **Option B** (Stored procedures are parsed, optimized, and compiled once on the database server, reusing cached query execution plans and reducing network round-trips)

---

### Question 88: [MCQ-088] Master-Slave Flip-Flop Clock Triggering
- **Exam Source**: NIELIT 2016 MAR Scientist C - Section C: 41
- **Topic**: Digital Logic: Flip-Flops & Hardware Triggers &bull; Master-Slave Clock Edge Invariants
- **Difficulty**: Medium

**Question Statement**:
How does a Master-Slave J-K flip-flop eliminate the race-around condition that plagues level-sensitive J-K flip-flops when J=1 and K=1?

**Options**:
- A. By isolating input sampling to the Master on clock high, and transferring output to the Slave only on the falling clock edge
- B. By replacing J-K gates with D latches
- C. By eliminating the clock signal entirely
- D. By running on direct current battery power

**Correct Answer**: **Option A** (By isolating input sampling to the Master on clock high, and transferring output to the Slave only on the falling clock edge)

---

### Question 89: [MCQ-089] OS Access Matrix: Capability Lists vs Access Control Lists
- **Exam Source**: NIELIT 2020 Nov Scientist B: 88
- **Topic**: Operating Systems: Security & Access Control &bull; Protection Matrices and Capability Lists
- **Difficulty**: Medium

**Question Statement**:
In Operating System protection models based on the Access Matrix, what is the fundamental difference between an Access Control List (ACL) and a Capability List?

**Options**:
- A. ACLs are stored with the subjects (rows of matrix), while Capability Lists are stored with objects (columns of matrix)
- B. An ACL is object-centric (associating with each object a list of subjects and their rights), while a Capability List is subject-centric (associating with each subject a list of objects and permitted rights)
- C. ACLs apply only to network cards, while Capability Lists apply only to disk files
- D. Capability lists cannot be revoked

**Correct Answer**: **Option B** (An ACL is object-centric (associating with each object a list of subjects and their rights), while a Capability List is subject-centric (associating with each subject a list of objects and permitted rights))

---

### Question 90: [MCQ-090] Mandatory Access Control (MAC) & Multi-Level Security
- **Exam Source**: NIELIT 2017 Oct Scientist B: 62
- **Topic**: Operating Systems: Security & Access Control &bull; Bell-LaPadula and Multi-Level Security Rules
- **Difficulty**: Hard

**Question Statement**:
In Mandatory Access Control (MAC) under the Bell-LaPadula model, what do the 'Simple Security Property' and the '* -Property' (Star Property) mandate?

**Options**:
- A. Read-Up allowed, Write-Down allowed
- B. No Read-Up (a subject cannot read objects at a higher security level) and No Write-Down (a subject cannot write to objects at a lower security level)
- C. All users can read and write all objects freely
- D. Security levels change dynamically based on CPU load

**Correct Answer**: **Option B** (No Read-Up (a subject cannot read objects at a higher security level) and No Write-Down (a subject cannot write to objects at a lower security level))

---

### Question 91: [MCQ-091] Software Engineering: Role-Based Actor Specification in Use Cases
- **Exam Source**: NIELIT 2021 Dec Scientist B - Section B: 68
- **Topic**: Software Engineering: Roles & Access Control &bull; UML Actor Roles and Access Boundaries
- **Difficulty**: Easy

**Question Statement**:
In UML software engineering and system modeling, what does an 'Actor' in a Use Case diagram represent?

**Options**:
- A. An internal database table containing employee records
- B. An external entity (human role, external hardware, or external system) that interacts with the system to achieve a specific goal
- C. A software developer writing backend code
- D. A physical CPU processor core

**Correct Answer**: **Option B** (An external entity (human role, external hardware, or external system) that interacts with the system to achieve a specific goal)

---

### Question 92: [MCQ-092] Database Check Constraints vs Triggers for Range Invariants
- **Exam Source**: NIELIT 2016 DEC Scientist B: 54
- **Topic**: Triggers & Active Databases &bull; Integrity Invariant Enforcement Techniques
- **Difficulty**: Medium

**Question Statement**:
Why is a table-level 'CHECK (Age >= 18)' constraint preferred over a 'BEFORE INSERT OR UPDATE' Trigger for validating simple attribute range boundaries?

**Options**:
- A. Triggers cannot evaluate mathematical comparison operators like >=
- B. CHECK constraints are declarative, compiled directly into table metadata, and execute with significantly lower overhead and no procedural context-switching
- C. Triggers only execute when the database restarts
- D. CHECK constraints can only be created on Sunday

**Correct Answer**: **Option B** (CHECK constraints are declarative, compiled directly into table metadata, and execute with significantly lower overhead and no procedural context-switching)

---

### Question 93: [MCQ-093] SQL Correlated Subquery Pairwise Evaluation
- **Exam Source**: NIELIT 2022 Apr Scientist B: 39
- **Topic**: SQL Invariants & Declarative Constraints &bull; Subquery Pairwise Comparison Invariants
- **Difficulty**: Medium

**Question Statement**:
Consider query: 'SELECT Emp_Name FROM Employees WHERE (Dept_ID, Salary) IN (SELECT Dept_ID, MAX(Salary) FROM Employees GROUP BY Dept_ID)'. What does this query return?

**Options**:
- A. It generates a syntax error because SQL does not support pairwise tuple comparison
- B. It retrieves the names of all employees who earn the maximum salary within their respective department
- C. It returns the employee with the lowest salary across the company
- D. It returns all employees in department 10 only

**Correct Answer**: **Option B** (It retrieves the names of all employees who earn the maximum salary within their respective department)

---

### Question 94: [MCQ-094] Network Access Control: Packet Filtering vs Stateful Inspection
- **Exam Source**: NIELIT 2018 | Question: 82
- **Topic**: Computer Networks: Access Control & Security &bull; Firewall Access Control Lists and Packet Filtering
- **Difficulty**: Medium

**Question Statement**:
In network security access control, what is a primary limitation of a stateless Packet-Filtering Router (stateless firewall) compared to a Stateful Inspection Firewall?

**Options**:
- A. Stateless routers cannot filter by IP address
- B. Stateless routers inspect packets in isolation and cannot track TCP connection states (e.g. SYN, ESTABLISHED), making them vulnerable to spoofed ACK packets
- C. Stateful firewalls only operate at the Physical Layer
- D. Stateless routers consume more CPU memory than stateful firewalls

**Correct Answer**: **Option B** (Stateless routers inspect packets in isolation and cannot track TCP connection states (e.g. SYN, ESTABLISHED), making them vulnerable to spoofed ACK packets)

---

### Question 95: [MCQ-095] Edge-Triggered vs Level-Triggered Interrupt Handling in CPUs
- **Exam Source**: NIELIT 2021 Dec Scientist B: 110
- **Topic**: Computer Architecture: Interrupts & Execution &bull; Hardware Interrupt Triggering Modes
- **Difficulty**: Medium

**Question Statement**:
What critical hardware danger occurs if a peripheral device generates a Level-Triggered interrupt and the CPU's Interrupt Service Routine (ISR) fails to clear the interrupt flag on the device before re-enabling interrupts?

**Options**:
- A. The CPU immediately encounters an infinite interrupt loop, repeatedly re-entering the ISR as soon as interrupts are enabled
- B. The computer's hard drive is wiped
- C. The interrupt line permanently burns out physically
- D. The CPU switches to 16-bit real mode

**Correct Answer**: **Option A** (The CPU immediately encounters an infinite interrupt loop, repeatedly re-entering the ISR as soon as interrupts are enabled)

---

### Question 96: [MCQ-096] Database Cursor Lifecycle: Declare, Open, Fetch, Close
- **Exam Source**: NIELIT 2020 Nov Assistant A: 45
- **Topic**: Triggers & Active Databases &bull; Procedural Cursors and Iterative Processing
- **Difficulty**: Easy

**Question Statement**:
In relational database procedural programming (PL/SQL), what is the correct chronological sequence of operations in the lifecycle of an explicit database cursor?

**Options**:
- A. OPEN -> DECLARE -> FETCH -> CLOSE
- B. DECLARE -> OPEN -> FETCH -> CLOSE
- C. FETCH -> OPEN -> DECLARE -> CLOSE
- D. DECLARE -> FETCH -> OPEN -> CLOSE

**Correct Answer**: **Option B** (DECLARE -> OPEN -> FETCH -> CLOSE)

---

### Question 97: [MCQ-097] Schema Level Assertions in Relational Standards
- **Exam Source**: NIELIT 2019 Scientist B: 18
- **Topic**: SQL Invariants & Declarative Constraints &bull; Schema Assertions vs Procedural Logic
- **Difficulty**: Medium

**Question Statement**:
Under the SQL-92 standard, what SQL statement is used to define an integrity constraint that spans across multiple tables and must be satisfied by every database state?

**Options**:
- A. CREATE ASSERTION <name> CHECK (<condition>);
- B. ALTER TABLE <name> ADD CONSTRAINT MULTI;
- C. CREATE MULTI_CHECK <condition>;
- D. CREATE TRIGGER <name> ON ALL TABLES;

**Correct Answer**: **Option A** (CREATE ASSERTION <name> CHECK (<condition>);)

---

### Question 98: [MCQ-098] Relational Domain Constraints and Data Typing
- **Exam Source**: NIELIT 2017 July Scientist B: 66
- **Topic**: SQL Invariants & Declarative Constraints &bull; Domain Constraints and Value Sets
- **Difficulty**: Easy

**Question Statement**:
In relational database theory, what does a 'Domain Constraint' define for an attribute?

**Options**:
- A. The list of users permitted to query the column
- B. The set of all permissible atomic values (data type, size, format, and allowable value range) that the attribute can take
- C. The foreign key parent relation name
- D. The disk sector address where the attribute is physically stored

**Correct Answer**: **Option B** (The set of all permissible atomic values (data type, size, format, and allowable value range) that the attribute can take)

---

### Question 99: [MCQ-099] Concurrency Serializability Graph Cycle Detection
- **Exam Source**: NIELIT 2018 | Question: 50
- **Topic**: Transactions & Concurrency Control &bull; Precedence Graphs and Cycle Detection
- **Difficulty**: Hard

**Question Statement**:
Given schedule S: r1(X); r2(Y); w1(Y); w2(X); commit1; commit2. Constructing the precedence graph for S produces:

**Options**:
- A. A cycle between T1 and T2 (T1 -> T2 and T2 -> T1), proving the schedule is NOT conflict serializable
- B. An acyclic graph with topological order T1, T2
- C. A graph with no edges
- D. A tree structure with T1 as root

**Correct Answer**: **Option A** (A cycle between T1 and T2 (T1 -> T2 and T2 -> T1), proving the schedule is NOT conflict serializable)

---

### Question 100: [MCQ-100] Write-Ahead Logging WAL Protocol Rules
- **Exam Source**: NIELIT 2021 Dec Scientist B: 118
- **Topic**: Transactions & Concurrency Control &bull; WAL Protocol Flushing Rules
- **Difficulty**: Medium

**Question Statement**:
Under the Write-Ahead Logging (WAL) protocol, which rule MUST be enforced by the database buffer manager before a modified dirty data page can be written to disk?

**Options**:
- A. All active transactions must commit first
- B. The log record corresponding to the update (with its undo information) must be flushed to non-volatile disk BEFORE the dirty data page itself is written to disk
- C. The database index must be dropped and recreated
- D. The user session must be disconnected

**Correct Answer**: **Option B** (The log record corresponding to the update (with its undo information) must be flushed to non-volatile disk BEFORE the dirty data page itself is written to disk)

---

## Section 4: UGC-NET Computer Science Questions (MCQ-101 to MCQ-178)

---

### Question 101: [MCQ-101] Event-Condition-Action (ECA) Rule Model & Triggers
- **Exam Source**: UGC NET CSE June 2013 | Part 3 | Question: 47
- **Topic**: Triggers & Active Databases &bull; ECA Model and Active Database Concepts
- **Difficulty**: Medium

**Question Statement**:
In active database architectures, which structural model pairs with 'Triggers' to govern automatic reactive rule processing?

**Options**:
- A. Private key encryption
- B. Event-Condition-Action (ECA) model
- C. Domain integrity constraints
- D. Relational calculus division

**Correct Answer**: **Option B** (Event-Condition-Action (ECA) model)

---

### Question 102: [MCQ-102] SQL Schema Assertions: CREATE ASSERTION Invariants
- **Exam Source**: UGC NET CSE June 2015 | Part 2 | Question: 16
- **Topic**: SQL Invariants & Declarative Constraints &bull; Schema-Level Assertions vs Single Table Checks
- **Difficulty**: Hard

**Question Statement**:
An Assertion is a predicate expressing a condition we wish the database to always satisfy. What is the correct SQL standard syntax for declaring an Assertion?

**Options**:
- A. CREATE ASSERTION <name> CHECK (<predicate>);
- B. ALTER TABLE <name> ADD ASSERTION (<predicate>);
- C. CREATE CONSTRAINT <name> ON DATABASE (<predicate>);
- D. CREATE TRIGGER <name> AS ASSERTION (<predicate>);

**Correct Answer**: **Option A** (CREATE ASSERTION <name> CHECK (<predicate>);)

---

### Question 103: [MCQ-103] SQL View Updatability & WITH CHECK OPTION Invariants
- **Exam Source**: UGC NET CSE Dec 2015 | Part 2 | Question: 18
- **Topic**: SQL Invariants & Declarative Constraints &bull; View Updatability and WITH CHECK OPTION
- **Difficulty**: Medium

**Question Statement**:
What is the effect of appending 'WITH CHECK OPTION' to a CREATE VIEW statement in SQL?

**Options**:
- A. It converts the view into an in-memory materialized snapshot
- B. It prevents any INSERT or UPDATE through the view that would produce rows that do not satisfy the view's WHERE clause
- C. It disables all foreign key checks on the underlying base tables
- D. It grants SELECT access to all public users

**Correct Answer**: **Option B** (It prevents any INSERT or UPDATE through the view that would produce rows that do not satisfy the view's WHERE clause)

---

### Question 104: [MCQ-104] Referential Integrity: Recursive Foreign Key Deletions
- **Exam Source**: UGC NET CSE Dec 2012 | Part 3 | Question: 70
- **Topic**: Referential Integrity & Cascades &bull; Foreign Key Deletion Traversal and Invariants
- **Difficulty**: Hard

**Question Statement**:
In a database enforcing referential integrity, if parent table P is referenced by child table C with ON DELETE RESTRICT, what occurs when a user executes 'DELETE FROM P WHERE P_ID = 10' when matching rows exist in C?

**Options**:
- A. Matching child rows in C are automatically deleted
- B. The deletion of the parent row in P is immediately prohibited and rolled back by the DBMS
- C. Matching rows in C have their foreign keys set to NULL
- D. The parent row is deleted and child rows become orphan tuples

**Correct Answer**: **Option B** (The deletion of the parent row in P is immediately prohibited and rolled back by the DBMS)

---

### Question 105: [MCQ-105] Database Security: Discretionary Access Control (DAC) via GRANT
- **Exam Source**: UGC NET CSE June 2014 | Part 2 | Question: 48
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Discretionary Access and Privilege Propagation
- **Difficulty**: Medium

**Question Statement**:
When user A executes 'GRANT SELECT ON Table1 TO UserB WITH GRANT OPTION', what capability has user A bestowed upon user B?

**Options**:
- A. User B can only read Table1, but cannot share the permission with others
- B. User B can read Table1 AND possesses the authority to grant SELECT privileges on Table1 to other database users
- C. User B becomes the database superuser
- D. User B can drop Table1

**Correct Answer**: **Option B** (User B can read Table1 AND possesses the authority to grant SELECT privileges on Table1 to other database users)

---

### Question 106: [MCQ-106] Cascade Option on REVOKE: Recursive Permission Withdrawal
- **Exam Source**: UGC NET CSE July 2016 | Part 2 | Question: 16
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; REVOKE CASCADE vs RESTRICT Invariants
- **Difficulty**: Hard

**Question Statement**:
User A grants privilege P to User B with grant option. User B grants P to User C. If User A executes 'REVOKE P FROM UserB CASCADE', what is the resulting authorization state of User C?

**Options**:
- A. User C retains privilege P because grants are immutable once bestowed
- B. Privilege P is recursively revoked from User C (and any users granted P by C) along the authorization dependency tree
- C. User C is promoted to take User B's place
- D. The revoke fails with a deadlock error

**Correct Answer**: **Option B** (Privilege P is recursively revoked from User C (and any users granted P by C) along the authorization dependency tree)

---

### Question 107: [MCQ-107] SQL Foreign Key Definition Syntax & Referential Actions
- **Exam Source**: UGC NET CSE Oct 2020 | Part 2 | Question: 96
- **Topic**: Referential Integrity & Cascades &bull; Declarative Foreign Key DDL Invariants
- **Difficulty**: Medium

**Question Statement**:
In SQL DDL, which clause correctly defines a foreign key in table Department(Dept_ID, Mgr_ID) referencing table Employee(Emp_ID) with automatic deletion propagation?

**Options**:
- A. FOREIGN KEY (Mgr_ID) REFERENCES Employee(Emp_ID) ON DELETE CASCADE
- B. FOREIGN KEY (Mgr_ID) EQUALS Employee(Emp_ID) CASCADE
- C. CONSTRAINT Mgr_ID MATCHES Employee(Emp_ID)
- D. LINK Mgr_ID TO Employee(Emp_ID) WITH DELETE

**Correct Answer**: **Option A** (FOREIGN KEY (Mgr_ID) REFERENCES Employee(Emp_ID) ON DELETE CASCADE)

---

### Question 108: [MCQ-108] ON DELETE SET NULL vs ON DELETE CASCADE Semantics
- **Exam Source**: UGC NET CSE Oct 2020 | Part 2 | Question: 97
- **Topic**: Referential Integrity & Cascades &bull; Referential Action Comparisons
- **Difficulty**: Medium

**Question Statement**:
What is the key functional difference between foreign key referential actions 'ON DELETE SET NULL' and 'ON DELETE CASCADE'?

**Options**:
- A. SET NULL deletes child rows, whereas CASCADE retains child rows with NULL values
- B. CASCADE deletes matching child rows when the parent row is deleted, whereas SET NULL retains matching child rows and updates their foreign key columns to NULL
- C. SET NULL can only be used on primary keys
- D. CASCADE is only supported in SQLite

**Correct Answer**: **Option B** (CASCADE deletes matching child rows when the parent row is deleted, whereas SET NULL retains matching child rows and updates their foreign key columns to NULL)

---

### Question 109: [MCQ-109] Composite Foreign Key Referential Matching
- **Exam Source**: UGC NET CSE Oct 2020 | Part 2 | Question: 98
- **Topic**: Referential Integrity & Cascades &bull; Composite Foreign Key Matching Semantics
- **Difficulty**: Hard

**Question Statement**:
In relational database schemas with composite keys, when a child table declares a composite foreign key (A, B) referencing parent table (P_A, P_B):

**Options**:
- A. The child row satisfies referential integrity if A matches any P_A regardless of B
- B. The combination of values (A, B) in the child tuple must exactly match the combined values (P_A, P_B) of a single tuple in the parent table (or both be NULL under MATCH FULL)
- C. Attribute A must be identical to attribute B in the child table
- D. Parent table must be unindexed

**Correct Answer**: **Option B** (The combination of values (A, B) in the child tuple must exactly match the combined values (P_A, P_B) of a single tuple in the parent table (or both be NULL under MATCH FULL))

---

### Question 110: [MCQ-110] Multiple Foreign Keys & Referential Cycles
- **Exam Source**: UGC NET CSE Oct 2020 | Part 2 | Question: 99
- **Topic**: Referential Integrity & Cascades &bull; Mutually Referencing Foreign Key Constraints
- **Difficulty**: Hard

**Question Statement**:
When table Department has a foreign key Manager_ID referencing Employee(Emp_ID), and table Employee has a foreign key Dept_ID referencing Department(Dept_ID), how can initial records be inserted without violating referential integrity?

**Options**:
- A. It is mathematically impossible to insert records into mutually referencing tables
- B. By inserting one table with a NULL foreign key first (or using DEFERRABLE constraints that delay foreign key checking until COMMIT), then inserting the second table, and updating the first
- C. By dropping both tables
- D. By disabling database logging permanently

**Correct Answer**: **Option B** (By inserting one table with a NULL foreign key first (or using DEFERRABLE constraints that delay foreign key checking until COMMIT), then inserting the second table, and updating the first)

---

### Question 111: [MCQ-111] SQL Schema Alteration with Foreign Key Constraints
- **Exam Source**: UGC NET CSE Oct 2020 | Part 2 | Question: 100
- **Topic**: SQL Invariants & Declarative Constraints &bull; ALTER TABLE and Constraint Addition Rules
- **Difficulty**: Medium

**Question Statement**:
If an administrator executes 'ALTER TABLE Child ADD CONSTRAINT fk_p FOREIGN KEY (P_ID) REFERENCES Parent(P_ID)' on a table already containing data, what check is performed by the database engine?

**Options**:
- A. The engine checks no data and applies the constraint only to future rows
- B. The engine validates all existing rows in Child; if any row has a P_ID that does not exist in Parent, the ALTER TABLE command fails and is rolled back
- C. The engine deletes all non-matching rows in Child automatically
- D. The engine populates missing rows in Parent with dummy data

**Correct Answer**: **Option B** (The engine validates all existing rows in Child; if any row has a P_ID that does not exist in Parent, the ALTER TABLE command fails and is rolled back)

---

### Question 112: [MCQ-112] Transaction Rollback & Log-Based Crash Recovery
- **Exam Source**: UGC NET CSE Dec 2014 | Part 3 | Question: 09
- **Topic**: Transactions & Concurrency Control &bull; Crash Recovery and Transaction States
- **Difficulty**: Hard

**Question Statement**:
During crash recovery using a Write-Ahead Log with checkpoints, which transactions must be UNDONE (rolled back)?

**Options**:
- A. All transactions that completed and committed before the checkpoint
- B. All transactions that were active (uncommitted) at the time of the crash
- C. All transactions recorded in the log from the start of the database
- D. Only read-only transactions

**Correct Answer**: **Option B** (All transactions that were active (uncommitted) at the time of the crash)

---

### Question 113: [MCQ-113] ACID Atomicity Enforcement via Undo Logging
- **Exam Source**: UGC NET CSE June 2012 | Part 2 | Question: 12
- **Topic**: Transactions & Concurrency Control &bull; Atomicity and Undo Log Mechanisms
- **Difficulty**: Medium

**Question Statement**:
In database recovery managers, what information stored in an update log record is used by the recovery engine to execute an UNDO operation?

**Options**:
- A. The New Value (after-image) of the modified data item
- B. The Old Value (before-image) of the modified data item
- C. The IP address of the client terminal
- D. The user's operating system password

**Correct Answer**: **Option B** (The Old Value (before-image) of the modified data item)

---

### Question 114: [MCQ-114] Concurrency Conflict Serializability Equivalence
- **Exam Source**: UGC NET CSE Nov 2017 | Part 3 | Question: 7
- **Topic**: Transactions & Concurrency Control &bull; Conflict Equivalence and Non-conflicting Swaps
- **Difficulty**: Medium

**Question Statement**:
Two transaction schedules S1 and S2 are defined as Conflict Equivalent if and only if:

**Options**:
- A. S1 and S2 contain the exact same transactions and order of all operations
- B. S1 can be transformed into S2 by a series of swaps of non-conflicting consecutive operations
- C. S1 and S2 produce the same final database state for only one specific initial state
- D. Both schedules use shared read locks exclusively

**Correct Answer**: **Option B** (S1 can be transformed into S2 by a series of swaps of non-conflicting consecutive operations)

---

### Question 115: [MCQ-115] View Serializability & Blind Writes
- **Exam Source**: UGC NET CSE June 2023 | Part 2: 44
- **Topic**: Transactions & Concurrency Control &bull; View Serializability and Blind Write Invariants
- **Difficulty**: Hard

**Question Statement**:
What condition allows a concurrent schedule to be View Serializable but NOT Conflict Serializable?

**Options**:
- A. The presence of shared read locks
- B. The presence of 'Blind Writes' (writing a data item without reading it first)
- C. Having only one transaction
- D. Using B-tree indexes

**Correct Answer**: **Option B** (The presence of 'Blind Writes' (writing a data item without reading it first))

---

### Question 116: [MCQ-116] Strict Two-Phase Locking vs Rigorous 2PL
- **Exam Source**: UGC NET CSE Oct 2020 | Part 2 | Question: 48
- **Topic**: Transactions & Concurrency Control &bull; Rigorous 2PL and Lock Holding Policies
- **Difficulty**: Hard

**Question Statement**:
How does 'Rigorous Two-Phase Locking' (Rigorous 2PL) differ from 'Strict 2PL' in relational transaction managers?

**Options**:
- A. Strict 2PL holds exclusive locks until commit, whereas Rigorous 2PL holds BOTH shared read locks AND exclusive write locks until transaction termination
- B. Rigorous 2PL allows locks to be released before commit
- C. Strict 2PL requires no lock manager
- D. Rigorous 2PL causes deadlocks in all schedules

**Correct Answer**: **Option A** (Strict 2PL holds exclusive locks until commit, whereas Rigorous 2PL holds BOTH shared read locks AND exclusive write locks until transaction termination)

---

### Question 117: [MCQ-117] Active Database Architecture: Event Detection
- **Exam Source**: UGC NET CSE Dec 2013 | Part 2 | Question: 12
- **Topic**: Triggers & Active Databases &bull; Active Database Subsystems and Event Detectors
- **Difficulty**: Medium

**Question Statement**:
In an Active Database Management System, which specialized subsystem is responsible for monitoring operations and signaling that a trigger's Event has taken place?

**Options**:
- A. Event Detector
- B. Query Optimizer
- C. Lock Manager
- D. Buffer Pool Manager

**Correct Answer**: **Option A** (Event Detector)

---

### Question 118: [MCQ-118] Row-Level Triggers vs Statement-Level Triggers
- **Exam Source**: UGC NET CSE Dec 2013 | Part 3 | Question: 60
- **Topic**: Triggers & Active Databases &bull; FOR EACH ROW vs FOR EACH STATEMENT Invariants
- **Difficulty**: Medium

**Question Statement**:
If an SQL statement 'UPDATE Employees SET Salary = Salary * 1.1 WHERE Dept_ID = 10' updates 50 employee records, how many times will a 'FOR EACH ROW' trigger execute compared to a 'FOR EACH STATEMENT' trigger?

**Options**:
- A. FOR EACH ROW executes 50 times; FOR EACH STATEMENT executes 1 time
- B. Both triggers execute 50 times
- C. Both triggers execute 1 time
- D. FOR EACH ROW executes 1 time; FOR EACH STATEMENT executes 50 times

**Correct Answer**: **Option A** (FOR EACH ROW executes 50 times; FOR EACH STATEMENT executes 1 time)

---

### Question 119: [MCQ-119] BEFORE INSERT Triggers: Data Sanitization & Invariants
- **Exam Source**: UGC NET CSE June 2009 | Paper 2: 23
- **Topic**: Triggers & Active Databases &bull; BEFORE Trigger Capabilities and Modifying NEW
- **Difficulty**: Medium

**Question Statement**:
What unique capability does a 'BEFORE INSERT' row-level trigger possess in relational database engines (such as PostgreSQL and Oracle) that an 'AFTER INSERT' trigger does NOT possess?

**Options**:
- A. It can modify the attributes of the 'NEW' record pseudo-variable before the tuple is written to the table
- B. It can drop the table
- C. It runs without acquiring database locks
- D. It can view deleted historical rows

**Correct Answer**: **Option A** (It can modify the attributes of the 'NEW' record pseudo-variable before the tuple is written to the table)

---

### Question 120: [MCQ-120] AFTER UPDATE Triggers: Automated Audit Trail Logging
- **Exam Source**: UGC NET CSE July 2018 | Part 2 | Question: 68
- **Topic**: Triggers & Active Databases &bull; Audit Trail Generation using AFTER Triggers
- **Difficulty**: Medium

**Question Statement**:
Why are 'AFTER UPDATE' triggers preferred over 'BEFORE UPDATE' triggers for recording historical change audit logs?

**Options**:
- A. AFTER triggers only run when the table is empty
- B. AFTER triggers fire only after the update has passed all declarative constraints and is guaranteed to succeed, preventing phantom audit entries for aborted updates
- C. BEFORE triggers cannot read the OLD record pseudo-variable
- D. AFTER triggers run with superuser permissions automatically

**Correct Answer**: **Option B** (AFTER triggers fire only after the update has passed all declarative constraints and is guaranteed to succeed, preventing phantom audit entries for aborted updates)

---

### Question 121: [MCQ-121] INSTEAD OF Triggers on Non-Updatable Complex Views
- **Exam Source**: UGC NET CSE July 2016 | Part 2 | Question: 20
- **Topic**: Triggers & Active Databases &bull; INSTEAD OF Triggers on Multi-Table Views
- **Difficulty**: Hard

**Question Statement**:
What is the primary architectural purpose of an 'INSTEAD OF' trigger in relational database management systems?

**Options**:
- A. Replacing deleted data with dummy data
- B. Intercepting DML operations (INSERT, UPDATE, DELETE) on non-updatable complex views and executing custom procedural code to modify underlying base tables
- C. Replacing B-tree indexes with hash tables
- D. Replacing SQL with Python syntax

**Correct Answer**: **Option B** (Intercepting DML operations (INSERT, UPDATE, DELETE) on non-updatable complex views and executing custom procedural code to modify underlying base tables)

---

### Question 122: [MCQ-122] Recursive Triggers & Cascading Trigger Depths
- **Exam Source**: UGC NET CSE June 2019 | Part 2 | Question: 35
- **Topic**: Triggers & Active Databases &bull; Trigger Cascading and Infinite Recursion
- **Difficulty**: Hard

**Question Statement**:
What occurs when Trigger A updates Table 2, firing Trigger B which updates Table 1, firing Trigger A again?

**Options**:
- A. The database executes the cycle indefinitely until physical RAM burns out
- B. The DBMS detects an infinite recursive trigger cascade, aborts the operation when the maximum trigger recursion depth is reached, and rolls back the transaction
- C. The database engine converts the trigger to a stored procedure
- D. The updates are saved in reverse chronological order

**Correct Answer**: **Option B** (The DBMS detects an infinite recursive trigger cascade, aborts the operation when the maximum trigger recursion depth is reached, and rolls back the transaction)

---

### Question 123: [MCQ-123] Database Roles: CREATE ROLE & GRANT ROLE Hierarchy
- **Exam Source**: UGC NET CSE Dec 2008 | Part 2 | Question: 34
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Inheritance
- **Difficulty**: Medium

**Question Statement**:
In enterprise Role-Based Access Control (RBAC), how is role inheritance established in SQL standard syntax?

**Options**:
- A. CREATE ROLE <child> EXTENDS <parent>;
- B. GRANT <parent_role> TO <child_role>;
- C. ALTER ROLE <child> INHERIT <parent>;
- D. SET ROLE <parent> INTO <child>;

**Correct Answer**: **Option B** (GRANT <parent_role> TO <child_role>;)

---

### Question 124: [MCQ-124] Privilege Revocation: RESTRICT vs CASCADE Invariants
- **Exam Source**: UGC NET CSE Dec 2009 | Part 2 | Question: 20
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; REVOKE RESTRICT Safety Semantics
- **Difficulty**: Medium

**Question Statement**:
Under the SQL standard, what occurs if an administrator executes 'REVOKE SELECT ON Table1 FROM UserA RESTRICT' when User A has previously granted SELECT to User B?

**Options**:
- A. SELECT is revoked from User A and User B simultaneously
- B. The REVOKE statement fails immediately with an error and no privileges are revoked
- C. User B becomes the owner of Table1
- D. Table1 is locked in read-only mode

**Correct Answer**: **Option B** (The REVOKE statement fails immediately with an error and no privileges are revoked)

---

### Question 125: [MCQ-125] WITH GRANT OPTION Delegation Chains & Cycles
- **Exam Source**: UGC NET CSE Jan 2017 | Part 2 | Question: 47
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Delegation Chains and Dual Path Grants
- **Difficulty**: Hard

**Question Statement**:
User A grants privilege P with grant option to User B. User B grants P to User C. Independently, User D (who also holds P with grant option) grants P to User C. If User A revokes P from User B CASCADE, what happens to User C's privilege?

**Options**:
- A. User C loses privilege P completely
- B. User C retains privilege P because an independent authorization path from User D still exists
- C. User C loses half of their permissions
- D. Both User B and User D are revoked

**Correct Answer**: **Option B** (User C retains privilege P because an independent authorization path from User D still exists)

---

### Question 126: [MCQ-126] Mandatory Access Control: Bell-LaPadula Simple Security
- **Exam Source**: UGC NET CSE June 2012 | Part 3 | Question: 8
- **Topic**: Operating Systems: Security & Access Control &bull; Multi-Level Security Models and Classifications
- **Difficulty**: Medium

**Question Statement**:
In multi-level security systems conforming to the Bell-LaPadula model, why is a subject with 'Secret' clearance forbidden from writing data into an 'Unclassified' document (No Write-Down)?

**Options**:
- A. To prevent the user from wasting hard disk space
- B. To prevent the illicit declassification or leakage of confidential information into lower-security publicly accessible channels
- C. Because unclassified documents cannot store binary characters
- D. Because Secret users can only read, not write

**Correct Answer**: **Option B** (To prevent the illicit declassification or leakage of confidential information into lower-security publicly accessible channels)

---

### Question 127: [MCQ-127] Relational Integrity & Cascade Semantics #1
- **Exam Source**: UGC NET CSE | Part 2 | Question: 51
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 101)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 128: [MCQ-128] Relational Integrity & Cascade Semantics #2
- **Exam Source**: UGC NET CSE | Part 2 | Question: 52
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 102)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 129: [MCQ-129] Relational Integrity & Cascade Semantics #3
- **Exam Source**: UGC NET CSE | Part 2 | Question: 53
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 103)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 130: [MCQ-130] Relational Integrity & Cascade Semantics #4
- **Exam Source**: UGC NET CSE | Part 2 | Question: 54
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 104)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 131: [MCQ-131] Relational Integrity & Cascade Semantics #5
- **Exam Source**: UGC NET CSE | Part 2 | Question: 55
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 105)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 132: [MCQ-132] Relational Integrity & Cascade Semantics #6
- **Exam Source**: UGC NET CSE | Part 2 | Question: 56
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 106)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 133: [MCQ-133] Relational Integrity & Cascade Semantics #7
- **Exam Source**: UGC NET CSE | Part 2 | Question: 57
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 107)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 134: [MCQ-134] Relational Integrity & Cascade Semantics #8
- **Exam Source**: UGC NET CSE | Part 2 | Question: 58
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 108)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 135: [MCQ-135] Relational Integrity & Cascade Semantics #9
- **Exam Source**: UGC NET CSE | Part 2 | Question: 59
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 109)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 136: [MCQ-136] Relational Integrity & Cascade Semantics #10
- **Exam Source**: UGC NET CSE | Part 2 | Question: 60
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 110)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 137: [MCQ-137] Relational Integrity & Cascade Semantics #11
- **Exam Source**: UGC NET CSE | Part 2 | Question: 61
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 111)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 138: [MCQ-138] Relational Integrity & Cascade Semantics #12
- **Exam Source**: UGC NET CSE | Part 2 | Question: 62
- **Topic**: Referential Integrity & Cascades &bull; Referential Actions & Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In relational schema management, how does the database engine maintain integrity when a parent record with referencing child tuples is modified under ON UPDATE CASCADE vs ON UPDATE RESTRICT (Case 112)?

**Options**:
- A. ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist
- B. RESTRICT deletes child records automatically
- C. CASCADE converts foreign keys to NULL
- D. Both actions disable foreign key checking

**Correct Answer**: **Option A** (ON UPDATE CASCADE propagates the primary key change to child foreign keys, whereas RESTRICT blocks the parent update if children exist)

---

### Question 139: [MCQ-139] Database Trigger Lifecycle & Timing Invariants #1
- **Exam Source**: UGC NET CSE | Part 3 | Question: 43
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 113)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 140: [MCQ-140] Database Trigger Lifecycle & Timing Invariants #2
- **Exam Source**: UGC NET CSE | Part 3 | Question: 44
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 114)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 141: [MCQ-141] Database Trigger Lifecycle & Timing Invariants #3
- **Exam Source**: UGC NET CSE | Part 3 | Question: 45
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 115)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 142: [MCQ-142] Database Trigger Lifecycle & Timing Invariants #4
- **Exam Source**: UGC NET CSE | Part 3 | Question: 46
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 116)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 143: [MCQ-143] Database Trigger Lifecycle & Timing Invariants #5
- **Exam Source**: UGC NET CSE | Part 3 | Question: 47
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 117)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 144: [MCQ-144] Database Trigger Lifecycle & Timing Invariants #6
- **Exam Source**: UGC NET CSE | Part 3 | Question: 48
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 118)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 145: [MCQ-145] Database Trigger Lifecycle & Timing Invariants #7
- **Exam Source**: UGC NET CSE | Part 3 | Question: 49
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 119)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 146: [MCQ-146] Database Trigger Lifecycle & Timing Invariants #8
- **Exam Source**: UGC NET CSE | Part 3 | Question: 50
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 120)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 147: [MCQ-147] Database Trigger Lifecycle & Timing Invariants #9
- **Exam Source**: UGC NET CSE | Part 3 | Question: 51
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 121)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 148: [MCQ-148] Database Trigger Lifecycle & Timing Invariants #10
- **Exam Source**: UGC NET CSE | Part 3 | Question: 52
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 122)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 149: [MCQ-149] Database Trigger Lifecycle & Timing Invariants #11
- **Exam Source**: UGC NET CSE | Part 3 | Question: 53
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 123)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 150: [MCQ-150] Database Trigger Lifecycle & Timing Invariants #12
- **Exam Source**: UGC NET CSE | Part 3 | Question: 54
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 124)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 151: [MCQ-151] Database Trigger Lifecycle & Timing Invariants #13
- **Exam Source**: UGC NET CSE | Part 3 | Question: 55
- **Topic**: Triggers & Active Databases &bull; Trigger Event Timing & Side Effect Isolation
- **Difficulty**: Medium

**Question Statement**:
In active database transaction processing, how are BEFORE vs AFTER triggers isolated with respect to statement-level rollback upon constraint failure (Case 125)?

**Options**:
- A. If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement
- B. BEFORE trigger side effects are permanently saved even if the statement fails
- C. AFTER triggers execute before constraints are evaluated
- D. Triggers run in a completely unlogged memory buffer

**Correct Answer**: **Option A** (If a constraint fails, any side effects performed by BEFORE triggers within the same transaction are rolled back along with the triggering statement)

---

### Question 152: [MCQ-152] Role-Based Security & Privilege Delegation #1
- **Exam Source**: UGC NET CSE | Part 2 | Question: 46
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 126)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 153: [MCQ-153] Role-Based Security & Privilege Delegation #2
- **Exam Source**: UGC NET CSE | Part 2 | Question: 47
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Medium

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 127)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 154: [MCQ-154] Role-Based Security & Privilege Delegation #3
- **Exam Source**: UGC NET CSE | Part 2 | Question: 48
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 128)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 155: [MCQ-155] Role-Based Security & Privilege Delegation #4
- **Exam Source**: UGC NET CSE | Part 2 | Question: 49
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Medium

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 129)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 156: [MCQ-156] Role-Based Security & Privilege Delegation #5
- **Exam Source**: UGC NET CSE | Part 2 | Question: 50
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 130)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 157: [MCQ-157] Role-Based Security & Privilege Delegation #6
- **Exam Source**: UGC NET CSE | Part 2 | Question: 51
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Medium

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 131)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 158: [MCQ-158] Role-Based Security & Privilege Delegation #7
- **Exam Source**: UGC NET CSE | Part 2 | Question: 52
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 132)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 159: [MCQ-159] Role-Based Security & Privilege Delegation #8
- **Exam Source**: UGC NET CSE | Part 2 | Question: 53
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Medium

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 133)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 160: [MCQ-160] Role-Based Security & Privilege Delegation #9
- **Exam Source**: UGC NET CSE | Part 2 | Question: 54
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 134)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 161: [MCQ-161] Role-Based Security & Privilege Delegation #10
- **Exam Source**: UGC NET CSE | Part 2 | Question: 55
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Medium

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 135)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 162: [MCQ-162] Role-Based Security & Privilege Delegation #11
- **Exam Source**: UGC NET CSE | Part 2 | Question: 56
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 136)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 163: [MCQ-163] Role-Based Security & Privilege Delegation #12
- **Exam Source**: UGC NET CSE | Part 2 | Question: 57
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Medium

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 137)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 164: [MCQ-164] Role-Based Security & Privilege Delegation #13
- **Exam Source**: UGC NET CSE | Part 2 | Question: 58
- **Topic**: Database Security & Access Control (RBAC/DCL) &bull; Role Hierarchies and Least Privilege
- **Difficulty**: Hard

**Question Statement**:
In enterprise SQL authorization, why does the Principle of Least Privilege mandate separating administrative roles (e.g. DBA, Auditor, Operator) rather than assigning full SUPERUSER privileges (Case 138)?

**Options**:
- A. To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty
- B. Because superuser accounts cannot execute SELECT queries
- C. To reduce the cost of database software licenses
- D. Because operating systems forbid root users

**Correct Answer**: **Option A** (To minimize attack surface and prevent accidental or malicious schema destruction by limiting each role to only the exact operations required for its duty)

---

### Question 165: [MCQ-165] Concurrency Serializability & Transaction Safety #1
- **Exam Source**: UGC NET CSE | Part 3 | Question: 49
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 139)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 166: [MCQ-166] Concurrency Serializability & Transaction Safety #2
- **Exam Source**: UGC NET CSE | Part 3 | Question: 50
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 140)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 167: [MCQ-167] Concurrency Serializability & Transaction Safety #3
- **Exam Source**: UGC NET CSE | Part 3 | Question: 51
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 141)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 168: [MCQ-168] Concurrency Serializability & Transaction Safety #4
- **Exam Source**: UGC NET CSE | Part 3 | Question: 52
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 142)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 169: [MCQ-169] Concurrency Serializability & Transaction Safety #5
- **Exam Source**: UGC NET CSE | Part 3 | Question: 53
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 143)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 170: [MCQ-170] Concurrency Serializability & Transaction Safety #6
- **Exam Source**: UGC NET CSE | Part 3 | Question: 54
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 144)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 171: [MCQ-171] Concurrency Serializability & Transaction Safety #7
- **Exam Source**: UGC NET CSE | Part 3 | Question: 55
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 145)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 172: [MCQ-172] Concurrency Serializability & Transaction Safety #8
- **Exam Source**: UGC NET CSE | Part 3 | Question: 56
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 146)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 173: [MCQ-173] Concurrency Serializability & Transaction Safety #9
- **Exam Source**: UGC NET CSE | Part 3 | Question: 57
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 147)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 174: [MCQ-174] Concurrency Serializability & Transaction Safety #10
- **Exam Source**: UGC NET CSE | Part 3 | Question: 58
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 148)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 175: [MCQ-175] Concurrency Serializability & Transaction Safety #11
- **Exam Source**: UGC NET CSE | Part 3 | Question: 59
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 149)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 176: [MCQ-176] Concurrency Serializability & Transaction Safety #12
- **Exam Source**: UGC NET CSE | Part 3 | Question: 60
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Hard

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 150)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 177: [MCQ-177] Concurrency Serializability & Transaction Safety #13
- **Exam Source**: UGC NET CSE | Part 3 | Question: 61
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 151)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

### Question 178: [MCQ-178] Concurrency Serializability & Transaction Safety #14
- **Exam Source**: UGC NET CSE | Part 3 | Question: 62
- **Topic**: Transactions & Concurrency Control &bull; Serializability and Invariant Guarantees
- **Difficulty**: Medium

**Question Statement**:
In multi-transaction concurrency control, why does an engine ensure that a transaction's serialization order matches its commit order under rigorous locking protocols (Case 152)?

**Options**:
- A. To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit
- B. To eliminate the need for primary keys
- C. To allow transactions to run without acquiring locks
- D. Because serial schedules are inherently slower

**Correct Answer**: **Option A** (To guarantee that external observers perceive database state transitions exactly in the real-time order transactions commit)

---

