class Solution {
    static Map<Integer, List<Integer>> map;
    static List<Integer> states;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // init states
        states = new ArrayList<>(Collections.nCopies(numCourses, 0));

        // neighbors map
        map = new HashMap<>();
        for (int[] pre: prerequisites) {
            List<Integer> neighbors = map.get(pre[1]);
            if (neighbors == null) {
                map.put(pre[1], new ArrayList<>(List.of(pre[0])));
            } else {
                neighbors.add(pre[0]);
            }
        }

        // dfs
        for (int node = 0; node < numCourses; node++) {
            if (states.get(node) == 0) {
                if (!isDagFromNode(node)) {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean isDagFromNode(int node) {
        if (states.get(node) == 1) {
            return false;
        } else if (states.get(node) == 2) {
            return true;
        }
        states.set(node, 1);
        if (map.containsKey(node)) {
            for (int neighbor: map.get(node)) {
                if (!isDagFromNode(neighbor)) {
                    return false;
                }
            }
        }
        states.set(node, 2);
        return true;
    }
}