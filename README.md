# 📐 Discrete Mathematics — Problem Solver

Collection of Python solutions for discrete mathematics problems, covering combinatorics and number theory. Each exercise includes a brute-force generator and an efficient solution, validated by an automated stress tester.

**Language:** Python 3

---

## 📁 Structure

```
discrete_maths/
├── Ejercicio de combinatoria/
│   ├── Simetric_and_Transitive.py   ← Efficient solution
│   ├── Generador.py                 ← Brute-force generator
│   └── Tester.py                    ← Stress tester
└── Ejercicio de teoría de números/
    ├── Monitor.py                   ← Efficient solution
    ├── Generador.py                 ← Brute-force generator
    └── Tester.py                    ← Stress tester
```

---

## 🔢 Exercise 1 — Combinatorics: Symmetric & Transitive Relations

**Problem:** Given `n`, count the number of relations on a set of `n` elements that are both symmetric and transitive, modulo `10⁹ + 7`.

**Approach (`Simetric_and_Transitive.py`):** Dynamic programming using a rolling index. Iterates over equivalence classes to count valid partitions, accumulating results in a circular array to avoid reallocation.

**Generator (`Generador.py`):** Generates a random `n` in [1, 4000] and computes the answer using a reference implementation based on precomputed factorials and the binomial coefficient identity for counting partitions.

**Tester (`Tester.py`):** Runs 30 random test cases, comparing the generator's reference answer against the efficient solution's output and printing a pass/fail per case.

### Running

```bash
cd "Ejercicio de combinatoria"

# Run the efficient solution (reads n from stdin)
echo 5 | python Simetric_and_Transitive.py

# Run the stress test (30 random cases)
python Tester.py
```

---

## 🔢 Exercise 2 — Number Theory: Monitor Problem

**Problem:** Given constraints `A`, `B`, `p`, `q`, find the largest values `x ≤ A` and `y ≤ B` such that `x/y = p/q` in lowest terms (i.e., `x` and `y` are the maximum multiples of the reduced fraction `p/q` that fit within the bounds).

**Approach (`Monitor.py`):** Reduces `p/q` using `gcd(p, q)`, then finds the largest integer `s` such that `s × (p/gcd) ≤ A` and `s × (q/gcd) ≤ B`. Returns `s × (p/gcd)` and `s × (q/gcd)`.

**Generator (`Generador.py`):** Generates random inputs `A`, `B`, `p`, `q` and computes the reference answer by iterating multiples of the reduced fraction.

**Tester (`Tester.py`):** Runs 30 random test cases, comparing generator and efficient solution outputs.

### Running

```bash
cd "Ejercicio de teoría de números"

# Run the efficient solution (reads "A B p q" from stdin)
echo "100 100 3 4" | python Monitor.py

# Run the stress test (30 random cases)
python Tester.py
```

---

## ⚙️ Requirements

```bash
pip install none  # standard library only
```

Python 3.6+ required. No external dependencies.
