### Arithmetic operator
| Operator | Return         | Example        |
|----------|----------------|----------------|
| +        | Addition       | $(( $a + $b )) |
| -        | Subtraction    | $(( $a - $b )) |
| *        | Multiplication | $(( $a * $b )) |
| /        | Quotient       | $(( $a / $b )) |
| %        | Remainder      | $(( $a % $b )) |

### Relational operator
###### Note : If return is true/false, it can be used as condition

| Operator       | Return                               | Example         |
|----------------|--------------------------------------|-----------------|
| -eq            | True if a equal to b                 | [[ $a -eq $b ]] |
| -ne            | True if a not equal b                | [[ $a -ne $b ]] |
| -gt            | True if a greater than b             | [[ $a -gt $b ]] |
| -ge            | True if a greater or equal to b      | [[ $a -ge $b ]] |
| -lt            | True if a less than b                | [[ $a -lt $b ]] |
| -le            | True if a less or equal to b         | [[ $a -le $b ]] |
| = (assignment) | Assign right operand to left operand | a=$b            |
| == (equality)  | True if a equal b                    | [[ $a == $b ]]  |
| != (not equal) | True if a not equal to b             | [[ $a != $b ]]  |
| >              | 1 if a greater than b else 0         | $(( $a > $b ))  |
| >=             | 1 if a greater or equal b else 0     | $(( $a >= $b )) |
| <              | 1 if a less than b else 0            | $(( $a < $b ))  |
| <=             | 1 if a less or equal b else 0        | $(( $a <= $b )) |
