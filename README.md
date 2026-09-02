# Dynamic Epistemic Logic

Applications of **Dynamic Epistemic Logic (DEL)** to multi-agent reasoning, with an extension of an existing implementation of **Action Models with Vocabulary Change (ACM)**.

> **Coursework:** This project was completed as part of coursework at IIT Delhi. The course provided the base implementation of Action Models with Vocabulary Change (ACM); the problem modeling, applications, and extensions described in this repository were my work.


## Overview

This project explores how agents' knowledge changes as they receive and reason about information.

The project applies standard DEL constructs including:

* Kripke models and epistemic accessibility relations
* Public announcements
* Common knowledge
* Product updates
* Action models

These concepts were used to model and solve multi-agent reasoning problems including **Muddy Children** and **Sally-Anne-Test**.

## Extension of Action Models with Vocabulary Change

The project also works with an existing implementation of **Action Models with Vocabulary Change (ACM)** and extends its use to model more expressive events.

The extended models represent:

* **Private events** — information observed by only selected agents.
* **Unobserved events** — events whose occurrence may be unknown to some agents.
* **Factual-changing events** — events that change the underlying facts of a model.
* Changes in agents' knowledge resulting from these events through product updates.

The framework was applied to scenarios such as the **Sally–Anne test**, where the information structure cannot be represented using public announcements alone.

## Problems and Applications

### Muddy Children

Modeled the classic multi-agent reasoning problem using epistemic models and successive public announcements to analyze how agents' knowledge evolves.

### Sally–Anne Test

Used the extended action-model framework to represent private and unobserved events and analyze how different agents acquire and update knowledge.

### Other Theory Problems

Applied epistemic reasoning to additional theoretical problems involving knowledge, ignorance, information disclosure, and multi-agent reasoning, using Kripke structures, accessibility relations, and product updates

## My Contribution

* Applied Dynamic Epistemic Logic concepts to formalize and analyze multi-agent reasoning problems.
* Worked with and extended an existing **Action Models with Vocabulary Change** implementation.
* Modeled private, unobserved, and factual-changing events and analyzed their effect on agents' knowledge.
* Used product updates to study the transformation of epistemic models following information-changing events.

## Key Concepts

`Kripke Models` · `Epistemic Logic` · `Dynamic Epistemic Logic` · `Action Models` · `Product Updates` · `Common Knowledge` · `Multi-Agent Reasoning`

## Technologies

* Python
* Dynamic Epistemic Logic
* Formal Methods

## Repository Structure

```text
.
├── a2/          # Implementations and problem solutions
├── docs/        # Project documentation
└── instructions.pdf
```

See the files in `docs/` for additional details about the models and solutions.
