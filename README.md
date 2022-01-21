# Davis-Putnam algorithm

Verify if a nonempty set of nontrivial clauses is satisfiable or not.

## Syntax for running the script:

When the script is run it will display "S = " and wait for the user's
input that must be a nonempty set of nontrivial clauses. The syntax
of the set can be like described below or the sign `¬` can be 
replaced by `-` sign and the comas and outer brackets are optional. 
For example, this is also a valid syntax for the set: 
`{-v1 -v2 -v4} {-v2 -v3} {v1 -v3} {v1 v4} {v3}`.

After introducing the set and pressing enter "var = " will be displayed. 
This will establish the order of the variables in the set in which the 
algorithm will be applied. This step can be skipped if you want the algorithm to 
use the lexicographic order. For example, if enter is introduced in the example below
instead of `v1, v3, v2` the script will consider the order `v1, v2, v3` for the variables.
Comas are also optional (`v1 v3 v2` is also valid).

> python davis_putnam.py
> 
> **S =** {{¬v1, ¬v2, ¬v4}, {¬v2, ¬v3}, {v1, ¬v3}, {v1, v4}, {v3}}
> 
> **var =** v1, v3, v2





