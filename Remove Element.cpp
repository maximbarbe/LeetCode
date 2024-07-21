class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = nums.size();
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] == val) {
                k -=1;
                nums[i] = 101;
            }    
        }
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] == 101) {
                for (int j = i; j < nums.size()-1;j++) {
                    swap(nums[j], nums[j+1]);
                }
            }
        }
        return k;
    }
};