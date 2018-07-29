(define (same-even-odd a b)
 a
 (if (= (remainder a 2) (remainder b 2))
  #t
  #f
 )
)

; not successful yet; reporting error "expecting integer, but cdr is provided. however i'm using car....
(define (same-parity x . z)
 (if (null? z)
  0
  (if (same-even-odd x (car z))

  (cons (car z) (same-parity (car z) . (cdr z))
  )
   (same-parity (car z) . (cdr z))
 )
 )

  )



