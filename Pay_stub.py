def currency_f0rmatter(number):
        """ FORMATS INTEGERS TO CURRENCY FORMAT, RETURNS STRING OBJ """
        res = '$ {:,.2f}'.format(number)
        return res

class Employee_form_data():
    """ A DUMMY PARTIAL CLASS ONLY TO CONTAIN INFO FROM EMPLOYEE
    -Employee(db.model) may be diff to inh- """
    def __init__(
        self,
        firstName='Selcuk',
        middleName='Attila',
        lastName='Turkoz',
        companyName='JAM Payroll',
        allowance=1,
        hourlyRate=44,
        hoursWorked= 80
        ):
        pass
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.companyName = companyName
        self.allowance = allowance
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked

    def __str__(self):
        pass
        msg = 'never gonna keep me down'
        return msg


class ModGeneratedPayStubFrom(Employee_form_data):
    def __init__(self, payCntYr2Dt = 2, *args, **kwargs):
        super(ModGeneratedPayStubFrom, self).__init__(*args, **kwargs)
        self.payCntYr2Dt = payCntYr2Dt
        self.allowance_regression_slope = -0.1067
        self.allowance_regression_intcpt = 2.0444 
        self.allowanceFactor = (self.allowance_regression_slope * self.allowance) +  self.allowance_regression_intcpt
        self.current = self.hoursWorked * self.hourlyRate
        self.year2date = payCntYr2Dt * self.current
        self.hourlyR4te = currency_f0rmatter(self.hourlyRate)
        self.curr3nt = currency_f0rmatter(self.current)
        self.year2d4te = currency_f0rmatter(self.year2date)
        self.social_security = currency_f0rmatter(self.current * self.allowanceFactor *9.3/150)
        self.social_security_year2date = currency_f0rmatter(self.current *  self.allowanceFactor *9.3 / 150 * payCntYr2Dt)
        self.medicare = currency_f0rmatter(self.current *  self.allowanceFactor *2.18 / 150)
        self.medicare_year2date = currency_f0rmatter(self.current * 2.18 / 150 *  self.allowanceFactor *payCntYr2Dt)
        self.futa = currency_f0rmatter(self.current * 0.90 * self.allowanceFactor / 150)
        self.futa_year2date = currency_f0rmatter(self.current * 0.90 / 150 *  self.allowanceFactor *payCntYr2Dt)
        self.co_unemp = currency_f0rmatter(self.current * 1.77 / 150)
        self.co_unemp_year2date = currency_f0rmatter(self.current * 1.77 / 150 * payCntYr2Dt)
        self.taxes = currency_f0rmatter(self.current * 11.48 / 150)
        self.taxes_year2date = currency_f0rmatter(self.current * 11.48 / 150 * payCntYr2Dt)
        self.net_pay = currency_f0rmatter(self.current * 138.52 / 150)
        self.net_pay_y2d = currency_f0rmatter(self.current * 138.52 / 150 * payCntYr2Dt)
    
    def __str__(self):
        msg = 'never gonna keep me down'
        return msg



class Pay_stub(Employee_form_data):
    def __init__(self, pay_count_year2date = 2 ):
        pass
        self.pay_count_year2date = pay_count_year2date
        self.current = self.hoursWorked * self.hourlyRate
        self.year2date = pay_count_year2date * self.current
        self.hourlyRate = currency_f0rmatter(self.hourlyRate)
        self.curr3nt = currency_f0rmatter(self.current)
        self.year2d4te = currency_f0rmatter(self.year2date)
        self.social_security = currency_f0rmatter(self.current * 9.3/150)
        self.social_security_year2date = currency_f0rmatter(self.current * 9.3 / 150 * pay_count_year2date)
        self.medicare = currency_f0rmatter(self.current * 2.18 / 150)
        self.medicare_year2date = currency_f0rmatter(self.current * 2.18 / 150 * pay_count_year2date)
        self.futa = currency_f0rmatter(self.current * 0.90/ 150)
        self.futa_year2date = currency_f0rmatter(self.current * 0.90 / 150 * pay_count_year2date)
        self.co_unemp = currency_f0rmatter(self.current * 1.77 / 150)
        self.co_unemp_year2date = currency_f0rmatter(self.current * 1.77 / 150 * pay_count_year2date)
        self.taxes = currency_f0rmatter(self.current * 11.48 / 150)
        self.taxes_year2date = currency_f0rmatter(self.current * 11.48 / 150 * pay_count_year2date)
        self.net_pay = currency_f0rmatter(self.current * 138.52 / 150)
        self.net_pay_y2d = currency_f0rmatter(self.current * 138.52 / 150 * pay_count_year2date)
    
    def __str__(self):
        msg = 'I get knocked down but I get up again'
        return msg
                
