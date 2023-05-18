/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    return new Promise((resolve,reject) => {
        let i = 0;
        let inprogess = 0;
        
        function callback() {
            if(i === functions.length && inprogess === 0){
                resolve();
            }
            while(i<functions.length && inprogess < n){
                functions[i++]()
                    .then(() => {
                        inprogess--;
                        callback();
                    });
                inprogess++;
            }
        }
        callback();
    });
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */