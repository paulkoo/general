class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prev = "", current = "";
        if (strs.length == 0) return prev;
        int len = strs[0].length();
        
        //find smallest length string
        for (String index: strs) {
            if (index.length() < len) 
                len = index.length();
        }
            
        
        int n = 1;
        while (n <= len) {
            //get substring of first index
            prev = strs[0].substring(0,n);

            //get substring from all other strings in array
            for (int i = 1; i < strs.length; i++) {
                current = strs[i].substring(0,n);
                if (!current.equals(prev)) 
                    return strs[i].substring(0,n-1);
                System.out.println(current);
            }
            n++;
        }
        
        
        return prev;
    }
}
