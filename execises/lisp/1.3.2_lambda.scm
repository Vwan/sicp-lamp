(define (f x y)
(let (a (+ (1 x * y))) (b (- (1 y)))
 x * a * a + y * b + a * b
))
(f 1 2)