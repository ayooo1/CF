/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    ret = [];
    for(let i = 0; i<arr.length; i++){
        if (fn(arr[i],i)){
            ret.push(arr[i])
        }
    }
    return ret;
};