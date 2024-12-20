---
title: Cirq
url: https://en.wikipedia.org/wiki/Cirq
language: en
categories: ["Category:Articles with example Python (programming language) code", "Category:Articles with short description", "Category:Quantum programming", "Category:Short description is different from Wikidata"]
references: 0
last_modified: 2024-12-19T14:54:37Z
---

# Cirq

## Summary

Cirq is an open-source framework for noisy intermediate scale quantum (NISQ) computers.

## Full Content

Cirq is an open-source framework for noisy intermediate scale quantum (NISQ) computers.

History
Cirq was developed by the Google AI Quantum Team, and the public alpha was announced at the International Workshop on Quantum Software and Quantum Machine Learning on July 18, 2018.  A demo by QC Ware showed an implementation of QAOA solving an example of the maximum cut problem being solved on a Cirq simulator.

Usage
Quantum programs in Cirq are represented by "Circuit" which is made up of a series of "Moments" representing slices of quantum gates that should be applied at the same time. The programs can be executed on local simulators or against hardware supplied by IonQ, Pasqal, Rigetti, and Alpine Quantum Technologies
The following example shows how to create and measure a Bell state in Cirq.

Printing the circuit displays its diagram

Simulating the circuit repeatedly shows that the measurements of the qubits are correlated.

Projects
OpenFermion
OpenFermion is a library that compiles quantum simulation algorithms to Cirq.

TensorFlow Quantum
TensorFlow Quantum is an extension of TensorFlow that allows TensorFlow to be used to explore hybrid classical-quantum machine learning algorithms.

ReCirq
ReCirq is a repository of research projects done using Cirq.

Qsim Cirq
Qsim is a high performance wave function simulator that leverages gate fusing, AVS/FMA instructions, and OpenMP to achieve fast simulation rates. Qsimcirq allows one to use qsim from within Cirq.


== References ==
