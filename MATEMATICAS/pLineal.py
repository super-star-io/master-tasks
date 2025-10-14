import pulp as plp

modelo=plp.LpProblem("ejemplo", sense=plp.LpMaximize)

x=plp.LpVariable(name="x",lowBound=0,upBound=float('inf'),cat='Continuous')
y=plp.LpVariable(name="y",lowBound=0,upBound=float('inf'),cat='Continuous')

modelo.setObjective(70*x+50*y)
modelo.addConstraint(4*x+3*y<=240,"restriccion1")
modelo.addConstraint(2*x+y<=100, "restriccion2") 
modelo.writeLP("ejempl001.1p")
modelo.solve(plp.HIGHS(msg=1))

print(x.varValue,y.varValue)
