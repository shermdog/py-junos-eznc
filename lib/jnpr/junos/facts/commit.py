def facts_commit(dev, facts):
    rsp = dev.rpc.get_system_uptime_information()
    last_commit = {}

    x = rsp.xpath('//last-configured-time')[0]

    last_commit['date_time'] = x.findtext('date-time')
    last_commit['user'] = x.findtext('user')
    last_commit['seconds'] = x.xpath('date-time')[0].get('seconds')

    dev.facts['last_commit'] = last_commit
