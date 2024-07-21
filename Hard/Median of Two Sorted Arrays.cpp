#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        
        
        
        vector<int> merged(n + m);
        merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), merged.begin());

        
        if ((n + m) % 2 != 0) {
            
            return (double)merged[(n + m) / 2];
        } else {
            
            return (double)(merged[(n + m - 1) / 2] + merged[(n + m) / 2]) / 2.0;
        }
    }
};
