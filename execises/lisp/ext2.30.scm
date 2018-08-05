(define (square a)
 (* a a)
)
(square 2)

(define (square-tree tree square)
 (cond ((null? tree) '())
  ((not (pair? tree)) (square tree))
  (else (cons (square-tree (car tree) square) (square-tree (cdr tree) square)))

 )
)



(square-tree
(list 1
(list 2 (list 3 4) 5)
(list 6 7)) square)
;(1 (4 (9 16) 25) (36 49))

;尚未跑通
(define (square-tree-map tree square)
 (map (lambda (sub-tree)
         (
           if ( (pair? sub-tree))
                (square-tree-map sub-tree square)
                (square sub-tree)

         )
      )
  tree
 )
)

(square-tree-map
(list 1
(list 2 (list 3 4) 5)
(list 6 7)) square)
;(1 (4 (9 16) 25) (36 49))