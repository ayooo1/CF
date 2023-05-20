/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let isThrottled = false;
    let nxtargs = undefined;
    return function(...args) {
        if(isThrottled){
            nxtargs = args;
        } else {
            fn(...args);
            isThrottled = true;
            setTimeout(helper,t);
        }

        function helper(){
            if(nxtargs){
                fn(...nxtargs);
                isThrottled = true;
                nxtargs = null;
                setTimeout(helper,t);
            } else {
                isThrottled = false;
            }
        }

  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */