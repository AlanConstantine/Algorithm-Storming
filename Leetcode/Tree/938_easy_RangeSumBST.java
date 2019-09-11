import java.util.ArrayList;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public static int rangeSumBST(TreeNode root, int L, int R) {
        if (root == null) {
            return 0;
        } else if (root.val < L) {
            return rangeSumBST(root.right, L, R);
        } else if (root.val > R) {
            return rangeSumBST(root.left, L, R);
        }
        return root.val + rangeSumBST(root.right, L, R) + rangeSumBST(root.left, L, R);
    }

    public static void preTraversal(TreeNode root) {
        ArrayList tmp = new ArrayList<Integer>();
        pre_recursive(root, tmp);
        for (int i = 0; i < tmp.length(); i++) {
            System.out.println(tmp.get(i));
        }
    }

    public static void pre_recursive(TreeNode root, ArrayList tmp) {
        if (root == null) {
            return;
        }
        tmp.add(root.val);
        recursive(root.left, tmp);
        recursive(root.right, tmp);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(2);
        TreeNode t1 = new TreeNode(1);
        TreeNode t2 = new TreeNode(5);
        TreeNode t3 = new TreeNode(6);
        TreeNode t4 = new TreeNode(3);
        root.left = t1;
        root.right = t2;
        t1.left = t3;
        t1.right = t4;
        System.out.println(rangeSumBST(root, 2, 4));
    }
}