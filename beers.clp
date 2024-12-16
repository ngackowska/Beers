
(deftemplate beer
    (slot question (type STRING) (default "nil"))
    (slot question-fact (type STRING) (default "nil"))
    (multislot answer (type STRING) (default "nil"))
)

(defrule scotland-yes
    (scotland yes)
    ?id <- (beer (answer ?x))
    =>
    (modify ?id (answer "Brew Dog"))
)

(defrule scotland-no
    (scotland no)
    ?id <- (beer (question ?x))
    =>
    (modify ?id (question "Do you sleep in a double-wide?"))
)

(defrule double-wide-yes
    (double-wide yes)
    ?id <- (beer (answer ?x))
    =>
    (modify ?id (answer "Counry Club Malt Liquor"))
)

(defrule double-wide-no
    (double-wide no)
    ?id <- (beer (question ?x))
    =>
    (modify ?id (question "Are you Bob or Doug McKenzie?"))
)

