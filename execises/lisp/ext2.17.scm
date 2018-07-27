(define (last-pair lst)
  (if (null? lst)
      0
      (last-pair (cdr lst))
      )
  )

(last-pair (list 2 3 4 5))
(last-pair (list 23 72 149 34))
(last-pair '())   ; error.....
