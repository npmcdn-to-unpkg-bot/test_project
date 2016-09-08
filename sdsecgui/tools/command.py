#_*_coding:utf-8_*_

import os

from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

#로그불러왓!
setLogDir()
logger = getLogger()


def excuteCmd(command):
    logger.debug("excuteCmd")
    f = os.popen(command)
    result = f.read()
    logger.debug("result" + result)
    return result


def parsingOutputToList(output):
    rows = output.splitlines()
    if rows:
        keyList = rows[1][1:-1].split("|")
        for idx, key in enumerate(keyList):
            keyList[idx] = key.lower().strip().replace(" ", "_")
        resultList = []
        for row in rows[3:-1]:
            resultDic = {}
            cols = row[1:-1].split("|")
            for idx, col in enumerate(cols):
                key = keyList[idx]
                value = col.strip()
                resultDic[key] = value
            resultList.append(resultDic)
        return resultList
    else:
        logger.debug("List is empty")
        return None


def getInstanceList():
    logger.debug("getInstanceList")
    output = excuteCmd("nova list --all-tenants")
    instanceList = parsingOutputToList(output)

    return instanceList

class Instance:
    def showInstanceById(self, id):
        logger.debug("showInstanceById")
        output = excuteCmd("nova show " + id)
        rows = output.splitlines()
        if rows:
            instanceDic = {
                "OS-DCF:diskConfig": "",
                "OS-EXT-AZ:availability_zone": "",
                "OS-EXT-SRV-ATTR:host": "",
                "OS-EXT-SRV-ATTR:hostname": "",
                "OS-EXT-SRV-ATTR:hypervisor_hostnam": "",
                "OS-EXT-SRV-ATTR:instance_name": "",
                "OS-EXT-SRV-ATTR:kernel_id": "",
                "OS-EXT-SRV-ATTR:launch_index": "",
                "OS-EXT-SRV-ATTR:ramdisk_id": "",
                "OS-EXT-SRV-ATTR:reservation_id": "",
                "OS-EXT-SRV-ATTR:root_device_name": "",
                "OS-EXT-SRV-ATTR:user_data": "",
                "OS-EXT-STS:power_state": "",
                "OS-EXT-STS:task_state": "",
                "OS-EXT-STS:vm_state": "",
                "OS-SRV-USG:launched_at": "",
                "OS-SRV-USG:terminated_at": "",
                "accessIPv4": "",
                "accessIPv6": "",
                "config_drive": "",
                "created": "",
                "description": "",
                "flavor": "",
                "hostId": "",
                "host_status": "",
                "id": "",
                "image": "",
                "key_name": "",
                "locked": "",
                "metadata": "",
                "name": "",
                "os-extended-volumes:volumes_attached": "",
                "progress": "",
                "public_network": "",
                "security_groups": "",
                "status": "",
                "tags": "",
                "tenant_id": "",
                "updated": "",
                "user_id": "",
            }
            for row in rows[3:-1]:
                cols = row[1:-1].split("|")
                key = cols[0].strip().replace(" ", "_")
                value = cols[1].strip()
                instanceDic[key] = value
            logger.debug(instanceDic)
            return instanceDic
        else:
            logger.debug(id + "에 해당하는 인스턴스가 없습니다.")
            return None
    def __init__(self, id):
        # tempList = self.parsingOutputToList(output)
        logger.debug("init")
        instanceDic = self.showInstanceById(id)
        self.os_dce = {}
        self.os_ext_az = {}
        self.os_ext_srv_attr = {}
        self.os_ext_sts = {}
        self.os_srv_usg = {}
        self.os_extended_volumes = {}
        self.os_dce["diskConfig"] =                    instanceDic["OS-DCF:diskConfig"]
        self.os_ext_az["availability_zone"] =          instanceDic["OS-EXT-AZ:availability_zone"]
        self.os_ext_srv_attr["host"] =                 instanceDic["OS-EXT-SRV-ATTR:host"]
        self.os_ext_srv_attr["hostname"] =             instanceDic["OS-EXT-SRV-ATTR:hostname"]
        self.os_ext_srv_attr["hypervisor_hostnam"] =   instanceDic["OS-EXT-SRV-ATTR:hypervisor_hostnam"]
        self.os_ext_srv_attr["instance_name"] =        instanceDic["OS-EXT-SRV-ATTR:instance_name"]
        self.os_ext_srv_attr["kernel_id"] =            instanceDic["OS-EXT-SRV-ATTR:kernel_id"]
        self.os_ext_srv_attr["launch_index"] =         instanceDic["OS-EXT-SRV-ATTR:launch_index"]
        self.os_ext_srv_attr["ramdisk_id"] =           instanceDic["OS-EXT-SRV-ATTR:ramdisk_id"]
        self.os_ext_srv_attr["reservation_id"] =       instanceDic["OS-EXT-SRV-ATTR:reservation_id"]
        self.os_ext_srv_attr["root_device_name"] =     instanceDic["OS-EXT-SRV-ATTR:root_device_name"]
        self.os_ext_srv_attr["user_data"] =            instanceDic["OS-EXT-SRV-ATTR:user_data"]
        self.os_ext_sts["power_state"] =               instanceDic["OS-EXT-STS:power_state"]
        self.os_ext_sts["task_state"] =                instanceDic["OS-EXT-STS:task_state"]
        self.os_ext_sts["vm_state"] =                  instanceDic["OS-EXT-STS:vm_state"]
        self.os_srv_usg["launched_at"] =               instanceDic["OS-SRV-USG:launched_at"]
        self.os_srv_usg["terminated_at"] =             instanceDic["OS-SRV-USG:terminated_at"]
        self.accessIPv4 =                              instanceDic["accessIPv4"]
        self.accessIPv6 =                              instanceDic["accessIPv6"]
        self.config_drive =                            instanceDic["config_drive"]
        self.created =                                 instanceDic["created"]
        self.description =                             instanceDic["description"]
        self.flavor =                                  instanceDic["flavor"]
        self.hostId =                                  instanceDic["hostId"]
        self.host_status =                             instanceDic["host_status"]
        self.id =                                      instanceDic["id"]
        self.image =                                   instanceDic["image"]
        self.key_name =                                instanceDic["key_name"]
        self.locked =                                  instanceDic["locked"]
        self.metadata =                                instanceDic["metadata"]
        self.name =                                    instanceDic["name"]
        self.os_extended_volumes["volumes_attached"] = instanceDic["os-extended-volumes:volumes_attached"]
        self.progress =                                instanceDic["progress"]
        self.public_network =                          instanceDic["public_network"]
        self.security_groups =                         instanceDic["security_groups"]
        self.status =                                  instanceDic["status"]
        self.tags =                                    instanceDic["tags"]
        self.tenant_id =                               instanceDic["tenant_id"]
        self.updated =                                 instanceDic["updated"]
        self.user_id =                                 instanceDic["user_id"]