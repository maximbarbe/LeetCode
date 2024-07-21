class Solution {
public:
    int hIndex(vector<int>& citations) {
        vector<int> h;
        h.assign(1001, 0);
        for (auto val:citations) {
            h[val] ++;
        }
        int cumulative = 0;
        for (int i = 1000; i > 0; i--) {
            cumulative += h[i];
            h[i] = cumulative;
            
            if (h[i] >= i) {
                return i;
            }
        }
        return 0;
    }
};