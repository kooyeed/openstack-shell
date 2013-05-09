# vim: tabstop=4 shiftwidth=4 softtabstop=4


from mytest.kooyeed.hiworld import controllers


def append_v1_routers(mapper, routers):
    hitony_controller = controllers.HiTony()
    mapper.connect('/hiworld',
                   controller=hitony_controller,
                   action='tony',
                   conditions=dict(method=['GET']))
