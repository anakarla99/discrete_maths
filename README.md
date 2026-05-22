# 📐 Discrete Mathematics — Problem Solver

Python solutions to two discrete mathematics problems from the University of Havana computer science curriculum, each with a brute-force generator and an efficient solution verified by a stress tester.

**Language:** Python 3

---

## 📁 Structure

```
Ejercicio de combinatoria/
├── Simetric_and_Transitive.py   ← Efficient O(n²) solution
├── Generador.py                  ← Brute-force generator for random test cases
└── Tester.py                     ← Stress tester (30 rounds, compares both solutions)

Ejercicio de teoría de números/
├── Monitor.py                    ← Efficient GCD-based solution
├── Generador.py                  ← Random test case generator
└── Tester.py                     ← Stress tester (30 rounds, compares both solutions)
```

---

## 🧮 Problems

### Ejercicio de combinatoria — Symmetric & Transitive Relations

**Input:** an integer `n`

**Output:** the number of relations on a set of `n` elements that are both symmetric and transitive, modulo 10⁹ + 7.

The efficient solution uses dynamic programming: `dp[i]` counts equivalence classes of size `i`, then accumulates the result using binomial coefficients.

```bash
echo "5" | python Simetric_and_Transitive.py
```

---

### Ejercicio de teoría de números — Monitor

**Input:** four integers `A B C D` on one line

**Output:** the largest pair `(x, y)` such that `x ≤ A`, `y ≤ B`, and `x/y = C/D` (reduced form), i.e. the maximum multiple of the reduced ratio that fits within both bounds.

The solution reduces `C/D` by their GCD, then finds the maximum multiplier `s = min(A // (C/gcd), B // (D/gcd))`.

```bash
echo "100 200 6 4" | python Monitor.py
```

---

## 🧪 Running the stress tester

Each `Tester.py` runs 30 rounds: generates a random input, passes it to both the generator (brute force) and the efficient solution, and prints whether outputs match.

```bash
cd "Ejercicio de combinatoria"
python Tester.py

cd "Ejercicio de teoría de números"
python Tester.py
```
