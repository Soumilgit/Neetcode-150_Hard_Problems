/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        return mergeLists(lists, 0, lists.length - 1);
    }

    private ListNode merge(ListNode a, ListNode b) {
        ListNode dummyHead = new ListNode(-1);
        ListNode c = dummyHead;

        while (a != null && b != null) {
            if (a.val <= b.val) {
                c.next = a;
                a = a.next;
            } else {
                c.next = b;
                b = b.next;
            }
            c = c.next;
        }
        c.next = (a != null) ? a : b;
        return dummyHead.next;
    }

    private ListNode mergeLists(ListNode[] lists, int l, int r) {
        if (l > r) {
            return null;
        }
        if (l == r) {
            return lists[l];
        }
        int m = (l + r) / 2;
        ListNode a = mergeLists(lists, l, m);
        ListNode b = mergeLists(lists, m + 1, r);

        return merge(a, b);
    }
}
