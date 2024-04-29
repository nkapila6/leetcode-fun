# Intuition
submission link: https://leetcode.com/problems/add-two-numbers/solutions/5087263/easiest-and-most-intuitive-solution-beats-68-runtimes-and-90-memory/

<!-- Describe your first thoughts on how to solve this problem. -->
My solution can be called more intuitive and creative. Rather than dabbling with linked lists directly, I tried to simplify the problem space by adding the numbers and converting into strings then parsing the string input one-by-one into a new LinkedList.

# Approach
<!-- Describe your approach to solving the problem. -->
Below is a step-by-step approach to my intuition indicated above.

- Extract numbers from LinkedList into a String
- Reverse the strings
- Parse the String as an Integer and add the numbers
- Parse the Integer output as a String and reverse again
- Create a new LinkedList with the new String
- Return the newly created LinkedList

# Complexity
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
* **Time complexity**: We have 3 loops here: 1st loop for reading input 1 of size m, 2nd loop for reading input 2 of size n, 3rd loop for creating a new LinkedList.
    - The time complexity for reading will be: $$O(m)$$ + $$O(n)$$
    - For string/integer conversions: $$O(m)$$ and $$O(n)$$ for converting input 1 and input 2.
    - Adding complexity is $$O(max(m,n))$$.
    - Conversion from integer to string is again $$O(max(m,n))$$.
    - To re-create LinkedList, adding 2 numbers will result in size of $$max(m,n)$$. The length could be $$max(m,n)+1$$.
        - Example: number 1 = 999 with m=3, number 2 = 11 with n=2, sum = 1010 and $$max(m,n)=3$$. Therefore, $$max(m,n)+1$$ seems like the right choice.
    - The final complexity for time can be approximated to be $$O(max(m,n))$$.

<!-- Add your space complexity here, e.g. $$O(n)$$ -->
* **Space complexity**: We have 3 things variables that use up space. The 2 number strings and the resultant Linked List.
    - The number strings: Will be size $$m$$ and size $$n$$, i.e. $$O(m+n)$$.
    - The resultant Linked List will be $$max(m,n)+1$$, i.e. $$O(max(m,n)+1)$$.
    - Overall space complexity will be: $$O(m+n)$$. The $$O(m+n)$$ term dominates the input size.

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def createLL_int(num: str):
    head = ListNode()
    current = head
    previous = head

    for x in num:
        current.val = int(x)
        previous = current
        new = ListNode()
        current.next = new
        current = new
    previous.next = None
    
    return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # this is a hack-job solution :)
        # extract the numbers from linkedlists into a string -> int
        # add the numbers and convert into str
        # represent each bit as a LL node

        # extracting info out of linky list
        ll1_num, ll2_num = str(), str()
        while l1:
            ll1_num = ll1_num + str(l1.val)
            l1 = l1.next

        while l2:
            ll2_num = ll2_num + str(l2.val)
            l2 = l2.next
        
        # reverse strings
        ll1_num = ll1_num[::-1]
        ll2_num = ll2_num[::-1]
        
        # add numbers and reverse
        ll3_num = str(int(ll1_num)+int(ll2_num))
        ll3_num = ll3_num[::-1]
        
        # create linked list
        l3 = createLL_int(ll3_num)
        return l3
```