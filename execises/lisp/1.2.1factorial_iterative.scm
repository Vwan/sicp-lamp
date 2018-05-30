(define (factorial n)
  (define (iter result count max)
    (if (> count max) result
	(iter (* count result) (+ count 1) max)
     )
    )
  (iter 1 1 n)
  )

(factorial 5)
