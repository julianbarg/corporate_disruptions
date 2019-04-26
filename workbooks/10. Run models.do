use "H:\jbarg\PycharmProjects\corporate_disruptions\preprocessed\pace_delta_3 2019-04-26.dta"
xtset name year, delta(3)

xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3, fe robust
xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3, fe
estimate store fe

xtreg recalls_3 high_turnover_3 revenue_3, fe robust
xtreg recalls_3 high_turnover_3 revenue_3, fe
estimate store fe2

xtreg recalls_3 high_turnover_3, fe robust
xtreg recalls_3 high_turnover_3, fe
estimate store fe3

xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3, re robust
xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3, re
estimate store re

xtreg recalls_3 high_turnover_3 revenue_3, re robust
xtreg recalls_3 high_turnover_3 revenue_3, re
estimate store re2

xtreg recalls_3 high_turnover_3, re robust
xtreg recalls_3 high_turnover_3, re
estimate store re3

hausman fe re
hausman fe2 re2
hausman fe3 re3

xtreg recalls_3 elevated_turnover_3 revenue_3 ceo_exit_3, fe robust
xtreg recalls_3 elevated_turnover_3 revenue_3, fe robust

xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3 ceo_and_high_turnover, fe robust

xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3 ceo_exit_during ceo_exit_1, fe robust

xtreg recalls_3 high_turnover_3 revenue_3 ceo_exit_3 year, fe robust
