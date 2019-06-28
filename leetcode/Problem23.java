package leetcode;

/**
 * Definition for singly-linked list.
 */

import java.util.LinkedList; 
import java.util.Queue;

public class Problem23 {
    public static void main(String []args) {
        Solution s = new Solution();
        ListNode[] lists = new ListNode[5];

        // NOTE: Create an array of single-linked lists here.

        s.mergeKLists(lists);
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        
        Queue<ListNode> q = new LinkedList<>();
        for (ListNode l: lists) {
            q.add(l);
        }
    
        while (q.size() > 1) {
            q.add(this.merge2Lists(q.remove(), q.remove()));
        }
        
        return q.remove();
    }
    
    private ListNode merge2Lists(ListNode l1, ListNode l2) {
        ListNode d = new ListNode(0);
        ListNode ptr = d;
        
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                d.next = l1;
                l1 = l1.next;
            } else {
                d.next = l2;
                l2 = l2.next;
            }
            d = d.next;
        }
        
        while (l1 != null) {
            d.next = l1;
            l1 = l1.next;
            d = d.next;
        }
        while (l2 != null) {
            d.next = l2;
            l2 = l2.next;
            d = d.next;
        }
        
        return ptr.next;
    }
}