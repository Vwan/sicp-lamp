(define (exponent x n)
  (if (= n 0)
      1
      (* x (exponent x (- n 1))))) 

(exponent 2 2) 
