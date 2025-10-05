# Kunitz-Type Protein Domain Classification using Profile Hidden Markov Models

This repository contains the data, scripts, and report for my Bioinformatics Master’s Degree project at the focused on building a **Profile Hidden Markov Model (HMM)** for the automatic classification of **Kunitz-type protein domains** based on structural alignment.

## Overview

The project aimed to construct and validate an HMM capable of recognizing the **Kunitz-type protease inhibitor domain**, a key structural motif found in proteins such as **Bovine Pancreatic Trypsin Inhibitor (BPTI)**.

By integrating **structural and sequence-based analyses**, the HMM was trained on representative Kunitz-domain structures and validated using a *2-fold cross-validation* approach on positive and negative protein datasets.

## Key Methods

- Protein structural alignment using PDBeFold

- Profile HMM construction with HMMER

- Performance evaluation using:
    - Accuracy
    - Matthews Correlation Coefficient (MCC)
    - ROC curve analysis

## Files

- [`./scripts`](./scripts/) - Folder containing the scripts used for the pipeline
- [`Project_HMM_Alessandro-Caula.pdf`](./Project_HMM_Alessandro-Caula.pdf) - Complete scientific report