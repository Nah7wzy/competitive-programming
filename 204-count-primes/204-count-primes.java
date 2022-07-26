class Solution {
    public int countPrimes(int n) {
        int[] state = new int[n];
        int count = 0;
            
        for(int i = 2; i < n; i++){
            if(state[i] != -1){
                count++;
                int mult = i + i;
                while(mult < n){
                    state[mult] = -1;
                    mult = mult + i;
                }
            }
        }
        
        return count;
    }
}