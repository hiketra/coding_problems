--Problem: Create a function that takes in a base-10 integer and returns a String
--of the roman numeral for numbers up to a 1000
numerals = [(1000, "M"), (900, "CM"), (500, "D"),
            (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "IV"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")]

toRomanNumerals :: Integer -> String
toRomanNumerals n
  | n == 0 = ""
  | otherwise = snd(predecessor) ++ toRomanNumerals(n - fst(predecessor))
  where predecessor = getPred(n)

getPred :: Integer -> (Integer, String)
getPred n = head(filter(\(x, _) -> (quot n x) >0) numerals)
