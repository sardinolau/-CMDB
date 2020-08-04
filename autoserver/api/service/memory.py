from api import models
def process_memory_info(host_object,memory_dict):
    '''
    处理接收的内存信息
    :param host_object:
    :param disk_dict:
    :return:
    '''
    if not memory_dict['status']:
        print('内存信息没有获取到')
        print('获取内存信息出错：',memory_dict['error'])
        return
    new_memory_dict = memory_dict['data']
    new_memory_slot_set=set(new_memory_dict)

    db_memory_queryset = models.Memory.objects.filter(server=host_object).all()
    db_memory_dict = {item.slot:item for item in db_memory_queryset}
    db_memory_slot_set=set(db_memory_dict)
    print(new_memory_dict)
    print('************')
    print(db_memory_dict)


    record_str_list = []
    #增加
    create_slot_set=new_memory_slot_set-db_memory_slot_set
    for slot in create_slot_set:
        models.Memory.objects.create(server=host_object,**new_memory_dict[slot])
        msg = "【新增内存】容量{capacity}，槽口{slot}，模型{model}，速率{speed}，厂商{manufacturer}，序列号{sn}".format(**new_memory_dict[slot])
        record_str_list.append(msg)
    #删除
    remove_slot_set = db_memory_slot_set-new_memory_slot_set
    if remove_slot_set:
        models.Memory.objects.filter(server=host_object,slot__in=remove_slot_set).delete()
    msg = "【删除内存】槽口：{}".format(','.join(remove_slot_set))
    record_str_list.append(msg)
    #修改
    update_slot_set = new_memory_slot_set & db_memory_slot_set
    tmp = []
    for slot in update_slot_set:
        for key,value in new_memory_dict[slot].items():
            old_value = getattr(db_memory_dict[slot],key)
            if value == old_value:
                continue
            msg = "内存{}，由{}变成了{}".format(key,old_value,value)
            tmp.append(msg)
            setattr(db_memory_dict[slot],key,value)
        if tmp:
            db_memory_dict[slot].save()

            row = "【修改内存】：槽位{}，更新内容{}".format(slot,':'.join(tmp))
            record_str_list.append(row)

    if record_str_list:
        models.AssetsRecord.objects.create(content='\n'.join(record_str_list),server=host_object)