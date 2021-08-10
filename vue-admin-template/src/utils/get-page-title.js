import defaultSettings from '@/settings'

const title = defaultSettings.title || '人才公会'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
