### Insertion Sort - Θ(n^2)

#### What is it?
For i = 1, 2, 3, ... n <br>
_insert_ A[i] into sort array A[0 : i-1]<br>
by pairwise swaps down to the correct position of the number that was initially A[i]

#### Example
Sorting in ascending order<br>
**Step 1**- | 5 | 2 | 4 | 6 | 1 | 3 |<br>
_key_ is A[i] => A[1] i.e. 2<br>
since A[0] is greater than the _key_ so we do a pairwise swap<br>
| 2 | 5 | 4 | 6 | 1 | 3 |<br>
**Step 2**- | 2 | 5 | 4 | 6 | 1 | 3 |<br>
_key_ is at A[2] i.e. 4<br>
another swap between A[1] and A[2]<br>
| 2 | 4 | 5 | 6 | 1 | 3 |<br>
**Step 3**- | 2 | 4 | 5 | 6 | 1 | 3 |<br>
_key_ is at A[3] i.e. 6<br>
no swaps happen at this Step
| 2 | 4 | 5 | 6 | 1 | 3 |<br>
**Step 4**- | 2 | 4 | 5 | 6 | 1 | 3 |<br>
_key_ is at A[4] i.e. 1<br>
So, using pairwise swaps to find the correct position<br>
swap 1<->6, 1<->5, 1<->4, 1<->2<br>
essentially doing 4 swaps to the point where we have the correct position<br>
| 1 | 2 | 4 | 5 | 6 | 3 |<br>
**Step 5**- | 1 | 2 | 4 | 5 | 6 | 3 |<br>
_key_ is at A[5] i.e. 3<br>
now 3 needs to be put at the correct position<br>
swap 3<->6, 3<->5, 3<->4<br>
| 1 | 2 | 3 | 4 | 5 | 6 |<br>

#### Analysis
Θ(n) steps in terms of key positions<br>
At any step we could need to do Θ(n) swaps<br>
So, each step is Θ(n) **compares & swaps**

### Binary Insertion Sort - Θ(nlogn)

#### What is it?
For i = 1, 2, 3, ... n <br>
_insert_ A[i] into sort array A[0 : i-1]<br>
by ~pairwise swaps~ **_binary search_** down to the correct position of the number that was initially A[i]

**Note:** Binary Insertion Sort gives Θ(nlogn) time for _compares_ not for _swaps_. For _swaps_ the worst case complexity would be Θ(n^2) as we would have to shift a lot of elements to the right/left when swapping pairwise.
