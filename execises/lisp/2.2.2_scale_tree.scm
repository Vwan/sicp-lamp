; define length to get size of a list
(define (length lst)
 (cond ( (null? lst)      0)
  ( (+ 1 (length (cdr lst))))
 )
)

(define (scale-tree lst factor)
 (cond
  ((null? lst) '())   ; 之前错将lst写成list，结果将树的顶点都计算在内了

        ((not (pair? lst))      (* lst factor)    ) ;判断是否是list，如果不是，则是叶子，计入
  (else (cons (scale-tree (car lst) factor) (scale-tree (cdr lst) factor)))

 )
)

(scale-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)) 10)
;(10 (20 (30 40) 50) (60 70))



