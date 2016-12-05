from openerp import http
from openerp.http import request
from openerp.addons.website_sale.controllers.main import QueryURL
from openerp.addons.website_sale.controllers.main import website_sale

class tour_detail_website(http.Controller):

    #=========================================================================================================================================
    # This is for Homepage

    @http.route(['/page/homepage'], type='http', auth="public", website=True)
    def tour_cate(self,**post):

        print "Home page ================== "
        # print " Self ======> ",self
        # print "Post =====>",post

        keep = QueryURL('/tour')
        res=request.env['product.public.category'].search([], offset=0, limit=None, order=None, count=False)

        # print "res=====>",res
        # for rec in res:
        #     print "\n res name",rec.name

        tour_id=request.env['product.template'].search([], offset=0, limit=None, order=None, count=False)

        print "tour_id=====>",tour_id
        for tours in tour_id:
            print "\ntour name  ====>",tours.name

        return request.render('website.homepage',{'res':res, 'tour_id':tour_id ,'keep':keep, 'company_id': request.env.user.company_id})

    #=========================================================================================================================================
    # ThisCode is for Tour page if category is found from home page it will come here and display only those data with category received

    @http.route(['/tour'], type='http', auth="public", website=True)
    def tour(self,category=None,search=None,**post):

        res=request.env['product.template'].search([], offset=0, limit=None, order=None, count=False)
        keep = QueryURL('/tour/detail')
        keep2 = QueryURL('/tour')
        r=[]
        if category != None:
            for i in res:
                for categ in i.public_categ_ids:
                    if str(category) == categ.name:
                        r.append(i.id)
            res=request.env['product.template'].browse(r)
            print "Category id is ============= ", res
            print "\n category name is = ",res.name

        elif search != None :
            res=request.env['product.template'].search([('name', 'ilike', str(search))], offset=0, limit=None, order=None, count=False)

        else:
            res=request.env['product.template'].search([], offset=0, limit=None, order=None, count=False)

        return request.render('tour_management.id_tour_page_template',{'res':res, 'keep':keep, 'keep2':keep2 , 'company_id': request.env.user.company_id})

    #=========================================================================================================================================
    #  This code is for a particular tour detail when user will select and one tour to display

    @http.route(['/tour/detail'], type='http', auth="public", website=True)
    def tour_detail(self, name=None, **post):

        tour = QueryURL('/tour')
        keep_book = QueryURL('/tour_login')

        res=request.env['product.template'].search([], offset=0, limit=None, order=None, count=False)
        print " Tour Detail ========= Tour Name", res

        flg = []
        for r in res:
            if r.name == str(name):
                flg.append(r.id)
        res = request.env['product.template'].browse(flg)

        return request.render('tour_management.id_tour_detail_temp',{'res':res,'keep' : tour,'keep_book':keep_book, 'company_id': request.env.user.company_id})

    #=========================================================================================================================================
    # This code is for login page when user will click on login or it will land when user wants to book a tour


    @http.route(['/tour_login'], type='http', auth="public", website=True)
    def login_detail(self,tour_id=None,**post):

        print "Tour Id Got from Tour Detail ===================================== >>>>>>> ", tour_id
        tour_id = request.env['product.template'].browse(int(str(tour_id)))

        print "After Tour Browse ==================== >>>>>> ",tour_id
        regis = QueryURL('/tour_registration')
        forgot_pwd = QueryURL('/forgot_password')
        login_check = QueryURL('/book_tour')

        return request.website.render('tour_management.id_tour_login_temp',{'tour_id' : tour_id,'keep':regis,'keep':forgot_pwd,'keep':login_check, 'company_id': request.env.user.company_id})

    #=========================================================================================================================================
    # This code is for Login Check if user already exist then travel to book page or else login page..

    @http.route(['/book_tour'],type='http', auth='public', website=True)
    def book_tour(self,**post):

        # print 'email==========>>>>',post.get('email')
        # print 'password==========>>>>',post.get('password')

        booking = QueryURL('/book_confirm')
        regis = QueryURL('/tour_registration')
        forgot_pwd = QueryURL('/forgot_password')
        login_check = QueryURL('/book_tour')
        keep_booked_tour = QueryURL('/booked_tour')

        print 'Book tour ============ Tour id = ',post.get('tour_id')

        email = str(post.get('email'))
        password = str(post.get('pwd'))
        tour_id = request.env['product.template'].browse(int(str(post.get('tour_id'))))
        print '::::::::::::::::tour_id',tour_id.id

        res = request.env['res.partner'].search([('email', '=', email), ('password', '=', password)])

        cus_id = res.id or 0
        print 'record set is ============== ', cus_id

        if cus_id == 0 :
            print 'Fail==========>>>>'
            return request.website.render('tour_management.id_tour_login_temp',{'tour_id' : tour_id,'keep':regis,'keep':forgot_pwd,'keep':login_check, 'company_id': request.env.user.company_id})
        else :
            print 'Success==========>>>>',cus_id
            return request.website.render('tour_management.id_tour_booking_temp',{'tour_id' : tour_id, 'cus_id':res, 'keep':booking, 'keep_booked_tour':keep_booked_tour, 'company_id': request.env.user.company_id})

    #=========================================================================================================================================
    # This code is for tour registration when new user will land here from login page

    @http.route(['/tour_registration'], type='http', auth="public", website=True)
    def registration_detail(self,tour_id=None,**post):

        keep = QueryURL('/tour_registration_create')
        print "\n\n\n\n tour id in reg _+_+_+_+_+_+_+++_+_+_+_+_",tour_id
        if tour_id != None:
            tour_id = request.env['product.template'].browse(int(str(tour_id)))
        print 'Tour Registration ================= tour id = ', tour_id
        return request.website.render('tour_management.id_tour_registration_temp',{'tour_id' : tour_id,'keep':keep, 'company_id': request.env.user.company_id})


    # This code is when Registration details are filled and it is created in module in res.partner then it will transfer here

    @http.route(['/tour_registration_create'], type='http', auth="public", website=True)
    def tour_registration_create(self,tour_id=None,**post):

        name = str(post.get('name'))
        phone = str(post.get('phone'))
        email = str(post.get('email'))
        gender = str(post.get('gender'))
        user_id = str(post.get('user_id'))
        password = str(post.get('password'))

        print 'After registration ============= tour id = ', tour_id

        vals = {'name':name,'phone':phone,'email':email,'gender':gender,'user_id':user_id,'password':password, 'is_member':'True'}
        cus_id = request.env['res.partner'].create(vals).id or 0
        keep = QueryURL('/tour_login')

        if tour_id != None:
            tour_id = request.env['product.template'].browse(int(str(tour_id)))
        if cus_id == 0 :
            print 'Fail register  ==========>>>> ', cus_id
        else :
            print 'Seccessfully Registered  ==========>>>>', cus_id
            return request.website.render('tour_management.id_tour_login_temp',{'tour_id' :tour_id,'keep':keep, 'company_id': request.env.user.company_id})

    #=========================================================================================================================================
    # this code for the forgot password page

    @http.route(['/forgot_password'], type='http', auth="public", website=True)
    def forgot_detail(self,tour_id=None,**post):

        keep = QueryURL('/tour_forgot_password_create')

        print 'forgot password ========= tour id = ',str(post.get('tour_id')),tour_id
        if tour_id != None:
            tour_id = request.env['product.template'].browse(int(str(tour_id)))
        return request.website.render('tour_management.id_tour_forgot_password_temp',{'tour_id' : tour_id,'keep':keep, 'warning':'no', 'company_id': request.env.user.company_id})


    # This code  will check and update old the password with the new password in database with the existing user email id

    @http.route(['/tour_forgot_password_create'], type='http', auth="public", website=True)
    def tour_forgot_password_create(self,tour_id=None,**post):

        email = post.get('email')
        user_id = post.get('user_id')
        password = str(post.get('password'))
        res_obj =  request.env['res.partner']
        if tour_id != None:
            tour_id = request.env['product.template'].browse(int(str(tour_id)))

        print 'Email of the User in Forgot Password Page ======= ',email
        print 'After Password has change =========== tour id = ', tour_id

        # tour_id = request.env['product.template'].browse(int(str(post.get('tour_id'))))

        if email != 'None':
            print "Got email ============== ", post.get('email')
            res = res_obj.search([('email','=', str(email))])
            if len(res.ids) == 0:
                print "\n\n\n no emil found to formgate password"
                keep = QueryURL('/tour_forgot_password_create')
                return request.website.render('tour_management.id_tour_forgot_password_temp',{'tour_id' : tour_id,'keep':keep, 'warning':'yes', 'company_id': request.env.user.company_id})
            else:
                print "\nres:----------",res
                res[0].password = password

        keep = QueryURL('/tour_login')
        return request.website.render('tour_management.id_tour_login_temp',{'tour_id' : tour_id,'keep':keep, 'company_id': request.env.user.company_id})


        # else :
        #     print 'there is no match found by id or email'
        #
        # # vals = {'password':password}
        #
        # # res_obj.browse(res).write(vals)
        # res[0].password = password
        # print "Record after the password has change ============= ",res_obj.browse(res).name,"passperd :----",res_obj.browse(res).password
        #
        # if tour_id != None:
        #     tour_id = request.env['product.template'].browse(int(str(tour_id)))
        # keep = QueryURL('/tour_login')
        # return request.website.render('tour_management.id_tour_login_temp',{'tour_id' : tour_id,'keep':keep})

    #=========================================================================================================================================
    #  This code is for the tourquery detail where we will take the passenger details.

    @http.route(['/book_confirm'], type='http', auth="public", website=True)
    def tour_booking(self,**post):

        keep_booked_tour = QueryURL('/booked_tour')

        print 'After booking has confirm Customer id is ======================== ',str(post.get('cus_id'))
        print "toru id is ===================",post.get('tour_id')

        tour_id = request.env['product.template'].browse(int(str(post.get('tour_id'))))
        print "\n\n\ntour_id:::::::::::::::::",tour_id
        cus_id = request.env['res.partner'].browse(int(str(post.get('cus_id'))))
        print "\n\n\ncus_id:::::::::::::::::",cus_id

        keep = QueryURL('/tour_booking_create')
        print '\n\n\n\n\n total :---------------------',int(str(post.get('no_of_adults')))+int(str(post.get('no_of_childs')))
        vals={'name':cus_id.id, 'phone': cus_id.phone,
              'email':cus_id.email, 'tour':tour_id.id,
              'adult_no':int(str(post.get('no_of_adults'))),
              'child_w_nobed_no':int(str(post.get('no_of_childs'))),
              'no_seats' : int(str(post.get('no_of_adults')))+int(str(post.get('no_of_childs')))
              }

        query_id = request.env['tour.query.detail'].create(vals)
        print '-------------->>>>>>>>.',query_id
        print '\n\n\n\n\n\n\nquery_id.no_seats-------------->>>>>>>>.',query_id.no_seats



        adult_list = []
        for i in range(int(str(post.get('no_of_adults')))):

            adult_name = str(post.get('adult_name'+str(i+1)))
            adult_age = str(post.get('adult_age'+str(i+1)))
            adult_gender = str(post.get('adult_gender'+str(i+1)))
            print "========",adult_gender

            if adult_gender == 'Male':
                adult_gender = 'male'
            elif adult_gender == 'Female':
                adult_gender = 'female'


            adult_list.append((0,0,{

                'name':adult_name,
                'age':adult_age,
                'gen':adult_gender,
                'travel_id1':query_id.id,

            }))

        print "adult_l========",adult_list
        query_id.adult = adult_list

        child_list = []
        for i in range(int(str(post.get('no_of_childs')))):

            child_name = str(post.get('child_name'+str(i+1)))
            child_age = str(post.get('child_age'+str(i+1)))
            child_gender = str(post.get('child_gender'+str(i+1)))
            print "========",adult_gender

            if child_gender == 'Male':
                child_gender = 'male'
            elif child_gender == 'Female':
                child_gender = 'female'


            child_list.append((0,0,{

                'name':child_name,
                'age':child_age,
                'gen':child_gender,
                'travel_id4':query_id.id,

            }))

        print "adult_l========",child_list
        query_id.child_w_nobed = child_list



        return request.website.render('tour_management.id_tour_booking_confirm_temp',{'tour_id':tour_id,'keep':keep, 'cus_id':cus_id, 'keep_booked_tour': keep_booked_tour, 'query_id':query_id, 'company_id': request.env.user.company_id})

    @http.route(['/booked_tour'], type='http', auth="public", website=True)
    def booked_tour(self,cus_id=None, **post):

        keep_booked_tour = QueryURL('/booked_tour')
        keep_edit_booked_tour = QueryURL('/edit_booked_tour')

        print 'cus_id bokked tour-----***************------======',cus_id , type(cus_id)
        cus_id = int(str(cus_id))
        cus_email = request.env['res.partner'].browse(cus_id).email
        query_rec = request.env['tour.query.detail'].search([('email','=',cus_email)])


        return request.website.render('tour_management.id_toor_booked_temp123',{'rec':query_rec, 'keep_edit_booked_tour':keep_edit_booked_tour, 'cus_id':request.env['res.partner'].browse(cus_id), 'keep_booked_tour':keep_booked_tour, 'company_id': request.env.user.company_id})

    @http.route(['/edit_booked_tour'], type='http', auth="public", website=True)
    def edit_booked_tour(self,query_id=None, **post):
        query_rec = request.env['tour.query.detail'].browse(int(query_id))
        print "Query_rec===============",query_rec

