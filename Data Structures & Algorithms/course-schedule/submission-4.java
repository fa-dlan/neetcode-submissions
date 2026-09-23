class Solution {
    static Map<Integer, List<Integer>> map;
    static List<Integer> states;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // init states
        Solution.states = new ArrayList<>(Collections.nCopies(numCourses, 0));

        // neighbors map
        Solution.map = new HashMap<>();
        for (int[] pre: prerequisites) {
            List<Integer> neighbors = Solution.map.get(pre[1]);
            if (neighbors == null) {
                Solution.map.put(pre[1], new ArrayList<>(List.of(pre[0])));
            } else {
                neighbors.add(pre[0]);
            }
        }

        // dfs
        for (int node = 0; node < numCourses; node++) {
            if (Solution.states.get(node) == 0) {
                if (!Solution.isDagFromNode(node)) {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean isDagFromNode(int node) {
        if (Solution.states.get(node) == 1) {
            return false;
        } else if (Solution.states.get(node) == 2) {
            return true;
        }
        Solution.states.set(node, 1);
        if (Solution.map.containsKey(node)) {
            for (int neighbor: Solution.map.get(node)) {
                if (!Solution.isDagFromNode(neighbor)) {
                    return false;
                }
            }
        }
        Solution.states.set(node, 2);
        return true;
    }
}