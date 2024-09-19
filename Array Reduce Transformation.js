/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var cur = init;
    for (const v of nums) {
        cur = fn(cur, v)
    }
    return cur
};