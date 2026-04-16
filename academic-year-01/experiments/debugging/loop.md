### Maestro Challenge
### Course: Python101
### Date: Jan 31 - 2026

**while loop**
- A while loop must always update the variable used in its condition - 
every iteration, no matter what.

```
count = 0
num = 5

while num < 51:
    if num % 3 == 0:
        count += 1

        num + 1 
    if count > 10:
        break

print("\nMultiples of 3 found:", count)
```
- This causes the loop runs forver
    - num + 1
    - calculate a value, then discard 
There us no assigment, so num never changes.

So the loop:
- never advances
- never exits naturally
- only stops if break is reached

**Hightlight**
- if num % 3 == 0:
    num += 1   # dangerous
- Cause infinitive loops when condition is false

- num + 1   # does nothing
- No assignment means no state change causes infinitive loop

**Mental Concept**
- Python does nothing unless it is assigned.


