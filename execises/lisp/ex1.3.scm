					;Exercise 1.3: Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.
(define (square x) (* x x ))
(define (sumx x y z) (
				      (begin (define min x))
				       
				       (cond ((> min y) (begin (define min y )))
					    ((> min z)  (begin (define min z))))
					    (- (+ (square x) (square y) (square z)) (sqaure min))
					    ))
				    
(square 2)
  (sumx 1 2 3)
