class Solution {
    List<String> out = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        rec("", n, n);
        return out;
    }

    void rec(String cur, int left, int right) {
        if (left == 0 && right == 0) {
            out.add(cur);
            return;
        }
        if (left > 0) {
            rec(cur + "(", left - 1, right);
        }
        if (right > left) {
            rec(cur + ")", left, right - 1);
        }
    }
}
