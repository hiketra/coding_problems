-- Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
--
-- 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
--
-- By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

-------------------------------
--initial brute-force solution:
-------------------------------

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

list = map fib [1..35]
--arbritrary limit... need to fix

filteredList = filter (\(x) -> (x `mod` 2==0) && (x<4000000)) list

answer = sum(filteredList)

----------------------------------------------------
--infinite list solution/no arbritrary index limit--
----------------------------------------------------

infinite_list = filter (\(x) -> (x `mod` 2==0)) (map fib [1..])
--filtering infinite fibonnaci list by multiples of 2

infinite_answer = sum(takeWhile (\(x) -> (x<4000000)) infinite_list)
--taking only the elemnts that are under 4 million and calculating the sum
