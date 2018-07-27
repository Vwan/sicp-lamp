(cons 1 2)
(cons 3 (cons 1 2))
(cons (cons 0 1) (cons 1 2))
(cons #\a (cons 3 "hello"))
(cons 'a' 3)
(cons a cons (3 "hello"))  ; this line will be errored
(cons #\a#\c 1)   ; error again?

					; exercise 1
(cons "hi" "everybody")
(cons 0 '())   ; remember the empty list
(cons 1 (cons 10 100))

(cons 1 (cons 10 (cons 100 '())))

(cons #\I (cons "saw" (cons 3 (cons "girls" '()))))
(cons "Sum of" (cons 1 (cons 2 (cons 3 (cons 4 '())))) ( cons ("is" cons (10 '()))))

					; exercise 2
(car (cons 0 '()))
(cdr '(0))
(car '((1 2 3) (4 5 6)))
(cdr '(1 2 3 . 4))
(cdr (cons 3 (cons 2 (cons 1 '()))))

(list 1 2)
(cons 1 (cons 2 '()))
(list 0)

(list 1 2 3 4)
(list '(1 2 3 4))
(list '(1 2) '(3 4))
(list)
