/**
 * @param {Function} fn
 */
function memoize(fn) {
    const dp = {}
    return function(...args) {
        const key = JSON.stringify(args)
        if(key in dp){
            return dp[key];
        }
        
        dp[key] = fn(...args)
        return dp[key]
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */