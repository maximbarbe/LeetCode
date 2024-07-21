class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int cur = nums[0];
        int k = nums.size();
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == cur) {
                nums[i] = 101;
                k -= 1;
            } else {
                cur = nums[i];
            }
        }
        sort(nums.begin(), nums.end());
        return k;
    }
};