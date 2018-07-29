(append (list 1 2) (list 3 4))

(define ( append_new list1 list2)
		     (if (null? list1)
			 list2
			 (cons (car list1) (append_new (cdr list1) list2))

			 )
		     ))

(append_new (list 1 2) (list 3 4))
