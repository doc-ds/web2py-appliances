
db.define_table('t_site',
    Field('id','id',
          represent=lambda id:SPAN(id,' ',A('view',_href=URL('site_read',args=id)))),
    Field('f_name', type='string', notnull=True,
          label=T('Name')),
    Field('f_url', type='string', notnull=True,default='http://',
	      represent=lambda x: A(x, _href=x, _target='_blank'),
          label=T('Url')),
    Field('f_image', type='upload', notnull=True, default='',
          label=T('Screenshot'),comment='250x200, jpg'),
    Field('f_description', type='text',
          represent=lambda x: MARKMIN(x),
          comment='WIKI (markmin)',
          label=T('Description')),
    Field('f_featured', type='boolean', default=False,
          label=T('Featured'),writable=False,readable=False),
    Field('f_created_on','datetime',default=request.now,
          label=T('Created On'),writable=False,readable=False),
    Field('f_modified_on','datetime',default=request.now,
          label=T('Modified On'),writable=False,readable=False,
          update=request.now),
    Field('f_created_by',db.auth_user,default=auth.user_id,
          label=T('Created By'),writable=False,readable=False),
    Field('f_modified_by',db.auth_user,default=auth.user_id,
          label=T('Modified By'),writable=False,readable=False,
          update=auth.user_id),
    format='%(f_name)s',
    migrate=True)

