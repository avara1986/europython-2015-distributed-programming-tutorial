DISTRIBUTED PROGRAMMING WITH PYTHON
-----------------------------------
https://ep2015.europython.eu/conference/talks/distributed-programming-with-python

Francesco Pierfederici

Examples
========
Simulations

Teleconferencings app (Ej: Skype)

SETI@home, Folding@home

MMOG

Distributed rendering

Genomics applications


Requirements
============
Python 3.4 or 3.5


Parallel Computing
==================

The simultaneous use of more than one processor to solve a problem

Typically one or more processes on a single box

Typical tools of the trade include threads, Celerys

Distributed computing
=====================

The simultaneuous use of omre than one computer to solve a problem

Natural evolution when using process-based parallelism

Tools: queues, job schedules, CORBA, PyRO, MPI...


Mixed Paradigm
==============
Most often than not you will use a mixture or distributed computing and parallelism

The problem
^^^^^^^^^^^
Do something cpu-bound as fast as possible

Compute fibonacci numbers

We will use the 4 physucak threads on this laptp

wil simulate other machines on the network with VMs


Amandahls Law
^^^^^^^^^^^^^
Given an algorithhm with some part that cannot be run in parallel (fraction s) and athe rest that can (fraction p) and that takes t seconds on a single processor, then on n processors it will take

t(n) >_ s * t + (p*t)/n
