use "H:\jbarg\PycharmProjects\corporate_disruptions\preprocessed\pace_delta_3 2019-04-23.dta"
xtset name year, delta(3)
xtreg recalls_3 high_turnover_3 revenue_1 ceo_exit_3, fe vce(cluster name)
xtreg recalls_3 high_turnover_3 revenue_1, fe vce(cluster name)
